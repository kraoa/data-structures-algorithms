"""Tests for Problem. Verifies stored expected values via a DP reference."""

import unittest
from typing import List

from coins import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _coin_change_dp(coins: List[int], amount: int) -> int:
        """Standard O(amount × |coins|) bottom-up DP reference."""
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
        return dp[amount] if dp[amount] != INF else -1

    def test_expected_values_match_dp(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._coin_change_dp(tc.coins, tc.amount)
            self.assertEqual(
                tc.expected, ref,
                f"coins={tc.coins}, amount={tc.amount}: stored={tc.expected}, dp={ref}",
            )

    def test_dp_zero_amount(self) -> None:
        self.assertEqual(self._coin_change_dp([1, 5], 0), 0)

    def test_dp_impossible(self) -> None:
        self.assertEqual(self._coin_change_dp([2], 3), -1)

    def test_dp_greedy_fails(self) -> None:
        # Greedy picks 11+1+1+1+1=5 coins; optimal is 5+5+5=3.
        self.assertEqual(self._coin_change_dp([1, 5, 11], 15), 3)


if __name__ == "__main__":
    unittest.main()
