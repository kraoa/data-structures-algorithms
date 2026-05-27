"""Read this first."""

import copy
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class TestCase:
    grid: List[List[str]]  # '1' = land, '0' = water
    expected: int          # number of islands


class Problem:
    """
    Given an m×n grid of '1' (land) and '0' (water), return the number of
    islands. An island is a group of adjacent (horizontally or vertically)
    land cells surrounded by water.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.num_islands(grid) for each test case.
        solver must expose .num_islands(grid: List[List[str]]) -> int.
        A deep copy of the grid is passed; solvers may modify it freely.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.num_islands(copy.deepcopy(tc.grid))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([                             # LeetCode example 1 → 1 island
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"],
            ], 1),
            TestCase([                             # LeetCode example 2 → 3 islands
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"],
            ], 3),
            TestCase([["1"]],             1),
            TestCase([["0"]],             0),
            TestCase([["1","0","1","0"]], 2),      # alternating row
            TestCase([                             # all land → 1
                ["1","1"],
                ["1","1"],
            ], 1),
            # TestCase([...], ?),  # add your own
        ]
