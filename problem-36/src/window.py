"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expected: List[int]   # max of each sliding window of size k


class Problem:
    """
    Given an integer array and a window size k, slide the window from left to
    right and return the maximum value in each window position.

    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3
             → [3, 3, 5, 5, 6, 7]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        """
        Calls solver.max_sliding_window(nums, k) for each test case.
        solver must expose .max_sliding_window(nums: List[int], k: int) -> List[int].
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.max_sliding_window(list(tc.nums), tc.k)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),  # LeetCode example 1
            TestCase([1],                          1, [1]),                   # LeetCode example 2
            TestCase([1, -1],                      1, [1, -1]),               # k=1: each element
            TestCase([9, 11],                      2, [11]),                  # single window
            TestCase([4, -2],                      2, [4]),
            TestCase([2, 1, 5, 3, 6, 4, 8, 7],    4, [5, 6, 6, 8, 8]),
            # TestCase([???], ??, [???]),  # add your own
        ]
