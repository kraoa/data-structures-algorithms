"""Tests for Problem. Verifies stored expected values via a BFS reference."""

import copy
import unittest
from collections import deque
from typing import List

from grid import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _count_islands_bfs(grid: List[List[str]]) -> int:
        """BFS flood-fill reference — correct but used only for test verification."""
        if not grid:
            return 0
        grid = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    q: deque = deque([(r, c)])
                    grid[r][c] = "0"
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append((nx, ny))
        return count

    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._count_islands_bfs(tc.grid)
            self.assertEqual(
                tc.expected, ref,
                f"grid size {len(tc.grid)}×{len(tc.grid[0])}: stored={tc.expected}, bfs={ref}",
            )

    def test_bfs_all_water(self) -> None:
        self.assertEqual(self._count_islands_bfs([["0","0"],["0","0"]]), 0)

    def test_bfs_diagonal_not_connected(self) -> None:
        # Diagonal cells do NOT count as connected.
        self.assertEqual(self._count_islands_bfs([["1","0"],["0","1"]]), 2)

    def test_bfs_single_cell(self) -> None:
        self.assertEqual(self._count_islands_bfs([["1"]]), 1)
        self.assertEqual(self._count_islands_bfs([["0"]]), 0)


if __name__ == "__main__":
    unittest.main()
