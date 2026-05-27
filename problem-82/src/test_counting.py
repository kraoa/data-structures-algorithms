"""Tests for the Counting driver."""

import unittest
from functools import lru_cache

from counting import Counting, TestCase


def _brute_force(s: str, t: str) -> int:
    """Recursive memoized reference: count distinct subsequences."""
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if j == 0:
            return 1
        if i == 0:
            return 0
        result = dp(i - 1, j)
        if s[i - 1] == t[j - 1]:
            result += dp(i - 1, j - 1)
        return result

    return dp(len(s), len(t))


class TestCountingDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Counting.get_test_cases():
            self.assertEqual(
                tc.expected,
                _brute_force(tc.s, tc.t),
                msg=f"Mismatch for s={tc.s!r}, t={tc.t!r}",
            )

    def test_empty_both_strings(self) -> None:
        self.assertEqual(_brute_force("", ""), 1)

    def test_empty_s_nonempty_t(self) -> None:
        self.assertEqual(_brute_force("", "a"), 0)


if __name__ == "__main__":
    unittest.main()
