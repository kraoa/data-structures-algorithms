"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    grid: List[List[int]]  # 0 = empty, 1 = fresh orange, 2 = rotten orange
    expected: int          # minutes until all fresh are rotten, or -1 if impossible


class Problem:
    """
    Every minute, each fresh orange that is 4-directionally adjacent to a rotten
    orange becomes rotten. Return the minimum number of minutes until no fresh
    oranges remain, or -1 if it is impossible.

    Example: [[2,1,1],[1,1,0],[0,1,1]] → 4
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.oranges_rotting(grid) for each test case.
        solver must expose .oranges_rotting(grid: List[List[int]]) -> int.
        A deep copy of the grid is passed; solvers may modify it freely.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.oranges_rotting(copy.deepcopy(tc.grid))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),   # LeetCode example 1
            TestCase([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),  # isolated fresh → -1
            TestCase([[0, 2]],                           0),   # no fresh oranges
            TestCase([[1]],                             -1),   # fresh with no rotten
            TestCase([[2, 2], [2, 2]],                  0),   # all rotten already
            TestCase([[1, 2]],                           1),   # one step
            # TestCase([[...]], ?),  # add your own
        ]
