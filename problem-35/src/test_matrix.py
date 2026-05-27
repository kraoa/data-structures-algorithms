"""Tests for Problem. Verifies stored expected values via an O(n³) brute-force."""

import unittest
from typing import List

from matrix import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(grid: List[List[str]]) -> int:
        """Try every (row, col, side) triple; expand while all cells are '1'."""
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        max_side = 0
        for r in range(m):
            for c in range(n):
                s = 1
                while r + s <= m and c + s <= n:
                    if all(grid[r + i][c + j] == "1" for i in range(s) for j in range(s)):
                        max_side = max(max_side, s)
                        s += 1
                    else:
                        break
        return max_side * max_side

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.grid)
            self.assertEqual(
                tc.expected, ref,
                f"stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_all_zeros(self) -> None:
        self.assertEqual(self._brute_force([["0", "0"], ["0", "0"]]), 0)

    def test_brute_force_single_row(self) -> None:
        self.assertEqual(self._brute_force([["1", "1", "1"]]), 1)


if __name__ == "__main__":
    unittest.main()
