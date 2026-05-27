"""Tests for the Paths driver."""

import unittest
from typing import List

from paths import Problem


class TestPathsDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(grid: List[List[int]]) -> int:
        """O(m*n) DP reference."""
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.grid)
            self.assertEqual(tc.expected, bf, f"grid={tc.grid!r}")


if __name__ == "__main__":
    unittest.main()
