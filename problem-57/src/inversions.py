"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: List[int]  # expected[i] = count of elements to the right of i that are smaller


class Problem:
    """
    Given an integer array nums, return a count array where count[i] is the
    number of elements to the right of nums[i] that are strictly smaller.

    Example: nums = [5,2,6,1] -> [2,1,1,0]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.count_smaller(list(tc.nums))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([5, 2, 6, 1],  [2, 1, 1, 0]),   # LeetCode example 1
            TestCase([-1, -1],      [0, 0]),           # LeetCode example 2
            TestCase([1],           [0]),              # single element
            TestCase([2, 0, 1],     [2, 0, 0]),
            TestCase([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),  # fully descending
            TestCase([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),  # fully ascending
            # TestCase([???], [???]),  # add your own
        ]
