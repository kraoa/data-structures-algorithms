"""Tests for the MinCuts driver."""

import unittest

from mincuts import MinCuts, TestCase


def _brute_force_min_cut(s: str) -> int:
    """O(n²) DP with precomputed palindrome table."""
    n = len(s)
    if n == 0:
        return 0

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for i in range(n - 1):
        is_pal[i][i + 1] = s[i] == s[i + 1]
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]

    dp = list(range(n))
    for i in range(1, n):
        if is_pal[0][i]:
            dp[i] = 0
            continue
        for j in range(1, i + 1):
            if is_pal[j][i]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[n - 1]


class TestMinCutsDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in MinCuts.get_test_cases():
            result = _brute_force_min_cut(tc.s)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for s={tc.s!r}",
            )

    def test_single_char_zero_cuts(self) -> None:
        self.assertEqual(_brute_force_min_cut("a"), 0)

    def test_whole_palindrome_zero_cuts(self) -> None:
        self.assertEqual(_brute_force_min_cut("racecar"), 0)


if __name__ == "__main__":
    unittest.main()
