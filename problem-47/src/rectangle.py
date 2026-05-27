"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    matrix: List[List[str]]   # cells are '0' or '1'
    expected: int              # area of the largest all-1 rectangle


class Problem:
    """
    Given an m×n binary matrix of '0's and '1's, find the largest rectangle
    containing only '1's and return its area.

    Hint: treat each row as a histogram (heights of consecutive '1's above it),
    then apply the "largest rectangle in histogram" technique per row.

    Example:
        matrix = [["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]]
        → 6  (3×2 rectangle in rows 1-2, cols 2-4)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.maximal_rectangle(matrix) for each test case.
        solver must expose .maximal_rectangle(matrix: List[List[str]]) -> int.
        Returns (test_case, actual, passed).
        """
        import copy
        results = []
        for tc in self.test_cases:
            actual = solver.maximal_rectangle(copy.deepcopy(tc.matrix))
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
                6,
            ),  # LeetCode example 1
            TestCase([["0"]], 0),                          # LeetCode example 2
            TestCase([["1"]], 1),                          # LeetCode example 3
            TestCase([["0","0"]], 0),
            TestCase([["1","1"],["1","1"]], 4),            # full 2×2
            TestCase([["1","0","1"],["1","1","1"]], 3),    # bottom row is best
            # TestCase([[???]], ??),  # add your own
        ]
