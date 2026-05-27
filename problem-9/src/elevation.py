"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    height: List[int]
    expected: int


class Problem:
    """
    Given n non-negative integers representing an elevation map where each bar
    has width 1, compute the total units of water that can be trapped.

    Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.trap(height) for each test case.
        solver must expose .trap(height: List[int]) -> int.
        A copy of height is passed to prevent mutation from affecting results.
        Returns (test_case, actual_result, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.trap(list(tc.height))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # LeetCode example 1
            TestCase([4, 2, 0, 3, 2, 5],                   9),   # LeetCode example 2
            TestCase([1, 0, 1],                             1),
            TestCase([3, 0, 2, 0, 4],                       7),
            TestCase([1, 1],                                0),   # no valley
            TestCase([1],                                   0),   # single bar
            TestCase([],                                    0),   # empty
            # TestCase([...], ?),                                  # add your own
        ]
