"""Tests for the Regions driver."""

import copy
import unittest
from collections import deque
from typing import List

from regions import Problem


class TestRegionsDriver(unittest.TestCase):

    @staticmethod
    def _reference_solve(board: List[List[str]]) -> List[List[str]]:
        """BFS from border cells; mark safe O's, then flip the rest."""
        b = copy.deepcopy(board)
        if not b or not b[0]:
            return b
        m, n = len(b), len(b[0])
        q: deque = deque()
        for r in range(m):
            for c in range(n):
                if (r in (0, m - 1) or c in (0, n - 1)) and b[r][c] == "O":
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            if 0 <= r < m and 0 <= c < n and b[r][c] == "O":
                b[r][c] = "S"
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    q.append((r + dr, c + dc))
        for r in range(m):
            for c in range(n):
                if b[r][c] == "O":
                    b[r][c] = "X"
                elif b[r][c] == "S":
                    b[r][c] = "O"
        return b

    def test_expected_values_match_reference(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._reference_solve(tc.board)
            self.assertEqual(tc.expected, ref, f"board={tc.board!r}")


if __name__ == "__main__":
    unittest.main()
