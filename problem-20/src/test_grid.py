"""Tests for Problem. Verifies stored expected values via a BFS reference."""

import copy
import unittest
from collections import deque
from typing import List

from grid import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _rotting_bfs(grid: List[List[int]]) -> int:
        """Multi-source BFS reference."""
        grid = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        queue: deque = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        max_time = 0
        while queue:
            r, c, t = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    max_time = t + 1
                    queue.append((nr, nc, t + 1))
        return max_time if fresh == 0 else -1

    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._rotting_bfs(tc.grid)
            self.assertEqual(
                tc.expected, ref,
                f"grid={tc.grid}: stored={tc.expected}, bfs={ref}",
            )

    def test_bfs_no_fresh(self) -> None:
        self.assertEqual(self._rotting_bfs([[0, 2]]), 0)
        self.assertEqual(self._rotting_bfs([[2, 2], [2, 2]]), 0)

    def test_bfs_isolated_fresh(self) -> None:
        self.assertEqual(self._rotting_bfs([[1]]), -1)

    def test_bfs_one_step(self) -> None:
        self.assertEqual(self._rotting_bfs([[2, 1]]), 1)


if __name__ == "__main__":
    unittest.main()
