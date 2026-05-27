"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: bool   # True if nums can be split into two equal-sum subsets


class Problem:
    """
    Given an integer array, determine if it can be partitioned into two subsets
    with equal sums. Each element must go into exactly one subset.

    Example: nums = [1, 5, 11, 5] → True  ({1,5,5} and {11})
             nums = [1, 2, 3, 5]  → False
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, bool, bool]]:
        """
        Calls solver.can_partition(nums) for each test case.
        solver must expose .can_partition(nums: List[int]) -> bool.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.can_partition(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 5, 11, 5],   True),   # LeetCode example 1
            TestCase([1, 2, 3, 5],   False),   # LeetCode example 2: odd total
            TestCase([1, 1],          True),   # trivial equal split
            TestCase([1],            False),   # single element: impossible
            TestCase([2, 2, 1, 1],    True),   # {2,1} and {2,1}
            TestCase([3, 3, 3, 4, 5], True),   # {3,3,3}=9 and {4,5}=9
            TestCase([1, 2, 5],      False),   # sum=8, target=4 not reachable
            # TestCase([???], ???),  # add your own
        ]
