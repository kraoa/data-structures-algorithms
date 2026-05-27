"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]   # sorted, then rotated at an unknown pivot; no duplicates
    target: int
    expected: int     # index of target, or -1 if not present


class Problem:
    """
    Given an integer array that was sorted in ascending order and then rotated
    at an unknown pivot, search for target in O(log n) time. Return its index,
    or -1 if not found. All values are distinct.

    Example: nums = [4,5,6,7,0,1,2], target = 0 -> 4
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.search(list(tc.nums), tc.target)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([4, 5, 6, 7, 0, 1, 2], 0,  4),  # LeetCode example 1
            TestCase([4, 5, 6, 7, 0, 1, 2], 3, -1),  # LeetCode example 2
            TestCase([1],                   0, -1),  # LeetCode example 3
            TestCase([1],                   1,  0),  # single element, found
            TestCase([3, 1],                1,  1),
            TestCase([3, 1],                3,  0),
            TestCase([5, 1, 3],             3,  2),
            TestCase([4, 5, 6, 7, 0, 1, 2], 4,  0),  # target at rotation start
            # TestCase([...], ???, ???),  # add your own
        ]
