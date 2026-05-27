"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    grid: List[List[int]]
    expected: int


class Problem:
    """
    Given an m x n grid filled with non-negative integers, find the path from
    the top-left to the bottom-right corner that minimises the sum of all
    numbers along the path. You may only move right or down.

    Example: grid = [[1,3,1],[1,5,1],[4,2,1]] -> 7  (1->3->1->1->1)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.min_path_sum(copy.deepcopy(tc.grid))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),   # LeetCode example 1
            TestCase([[1, 2, 3], [4, 5, 6]],             12),  # LeetCode example 2
            TestCase([[1]],                               1),   # single cell
            TestCase([[1, 2], [1, 1]],                   3),   # 2x2 grid
            TestCase([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5),   # all-ones 3x3
            TestCase([[5]],                               5),   # single-cell non-unit
            # TestCase([[...], [...]], ???),  # add your own
        ]
