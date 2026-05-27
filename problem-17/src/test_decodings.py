"""Tests for Problem. Verifies stored expected values via a DP reference."""

import unittest
from decodings import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _decode_dp(s: str) -> int:
        """Standard O(n) DP reference."""
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            two = int(s[i - 2: i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

    def test_expected_values_match_dp(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._decode_dp(tc.s)
            self.assertEqual(
                tc.expected, ref,
                f"s={repr(tc.s)}: stored={tc.expected}, dp={ref}",
            )

    def test_dp_leading_zero(self) -> None:
        self.assertEqual(self._decode_dp("0"), 0)
        self.assertEqual(self._decode_dp("06"), 0)

    def test_dp_two_digit_boundary(self) -> None:
        self.assertEqual(self._decode_dp("26"), 2)  # "BF" or "Z"
        self.assertEqual(self._decode_dp("27"), 1)  # only "BG" (27>26)

    def test_dp_all_ones(self) -> None:
        # "111" → "AAA", "AK", "KA" → 3 ways
        self.assertEqual(self._decode_dp("111"), 3)


if __name__ == "__main__":
    unittest.main()
