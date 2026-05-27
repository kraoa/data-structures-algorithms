"""Tests for the Interleaving driver."""

import unittest

from interleaving import Problem


class TestInterleavingDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(s1: str, s2: str, s3: str) -> bool:
        """2D DP reference."""
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                )
        return dp[m][n]

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.s1, tc.s2, tc.s3)
            self.assertEqual(tc.expected, bf, f"s1={tc.s1!r} s2={tc.s2!r} s3={tc.s3!r}")


if __name__ == "__main__":
    unittest.main()
