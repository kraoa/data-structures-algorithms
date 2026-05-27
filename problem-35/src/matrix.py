"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    grid: List[List[str]]   # cells are '0' or '1'
    expected: int            # area of the largest all-1 square


class Problem:
    """
    Given an m×n binary matrix of '0's and '1's, find the largest square
    containing only '1's and return its area.

    Example:
        grid = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
        → 4  (a 2×2 square)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.maximal_square(grid) for each test case.
        solver must expose .maximal_square(grid: List[List[str]]) -> int.
        Returns (test_case, actual, passed).
        """
        import copy
        results = []
        for tc in self.test_cases:
            actual = solver.maximal_square(copy.deepcopy(tc.grid))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]],
                4,
            ),  # LeetCode example 1: 2×2 square
            TestCase([["0","1"],["1","0"]], 1),  # LeetCode example 2: only 1×1
            TestCase([["0"]],               0),  # LeetCode example 3: all zeros
            TestCase([["1"]],               1),  # single '1'
            TestCase([["1","1"],["1","1"]], 4),  # full 2×2
            # TestCase([[???]], ??),  # add your own
        ]
