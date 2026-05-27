"""Tests for the Envelopes driver."""

import unittest
from typing import List

from envelopes import Problem


class TestEnvelopesDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(envelopes: List[List[int]]) -> int:
        """O(n^2) DP reference: longest strictly increasing chain by both dimensions."""
        if not envelopes:
            return 0
        env = sorted(envelopes)
        n = len(env)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if env[j][0] < env[i][0] and env[j][1] < env[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.envelopes)
            self.assertEqual(tc.expected, bf, f"envelopes={tc.envelopes!r}")


if __name__ == "__main__":
    unittest.main()
