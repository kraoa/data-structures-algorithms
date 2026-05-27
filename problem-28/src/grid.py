"""Read this first."""

from collections import deque
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    heights: List[List[int]]
    expected: List[List[int]]  # sorted list of [row, col] pairs


class Problem:
    """
    An m×n grid represents an island. The Pacific Ocean touches the top
    and left edges; the Atlantic Ocean touches the bottom and right edges.
    Rain water can flow from a cell to a 4-directionally adjacent cell
    with height ≤ the current cell (or off the island into an ocean).

    Return all cells from which water can flow to BOTH oceans.

    Example: heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],
                       [6,7,1,4,5],[5,1,1,2,4]]
             → [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in self.test_cases:
            raw = solver.pacific_atlantic([list(row) for row in tc.heights])
            actual = sorted(raw)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                [[1, 2, 2, 3, 5],
                 [3, 2, 3, 4, 4],
                 [2, 4, 5, 3, 1],
                 [6, 7, 1, 4, 5],
                 [5, 1, 1, 2, 4]],
                [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            ),
            TestCase([[1]], [[0, 0]]),           # single cell touches both oceans
            TestCase([[1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
            TestCase([[10, 10, 10], [10, 1, 10], [10, 10, 10]],
                     [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]),
            # TestCase([...], [...]),            # add your own
        ]
