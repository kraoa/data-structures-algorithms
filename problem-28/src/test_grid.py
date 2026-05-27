"""Driver tests — all must pass out of the box."""

import unittest
from collections import deque
from grid import Problem, TestCase


class TestGrid(unittest.TestCase):

    @staticmethod
    def _bfs_from(heights: list, seeds: list) -> set:
        """BFS from seed cells, moving to neighbours with height >= current."""
        m, n = len(heights), len(heights[0])
        visited = set(seeds)
        queue = deque(seeds)
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return visited

    def _reference(self, heights: list) -> list:
        m, n = len(heights), len(heights[0])
        pacific_seeds = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]
        atlantic_seeds = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m - 1)]
        pacific = self._bfs_from(heights, pacific_seeds)
        atlantic = self._bfs_from(heights, atlantic_seeds)
        return sorted([r, c] for r, c in pacific & atlantic)

    def test_expected_values_match_reference(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._reference(tc.heights))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"pacific_atlantic": lambda self, h: []})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, list)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
