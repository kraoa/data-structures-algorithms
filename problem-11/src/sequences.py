"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: int  # length of the longest strictly increasing subsequence


class Problem:
    """
    Given an integer array, return the length of the longest strictly
    increasing subsequence (LIS).

    Example: [10, 9, 2, 5, 3, 7, 101, 18] → 4  (e.g. [2, 3, 7, 101])

    O(n²) DP works. Aim for O(n log n) using patience sorting / binary search.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.length_of_lis(nums) for each test case.
        solver must expose .length_of_lis(nums: List[int]) -> int.
        A copy of nums is passed to prevent mutation from affecting results.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.length_of_lis(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([10, 9, 2, 5, 3, 7, 101, 18], 4),  # LeetCode example 1
            TestCase([0, 1, 0, 3, 2, 3],             4),  # LeetCode example 2
            TestCase([7, 7, 7, 7, 7, 7, 7],           1),  # all equal
            TestCase([1, 2, 3, 4, 5],                 5),  # already sorted
            TestCase([5, 4, 3, 2, 1],                 1),  # fully descending
            TestCase([1],                              1),
            TestCase([],                               0),
            # TestCase([...], ?),  # add your own
        ]
