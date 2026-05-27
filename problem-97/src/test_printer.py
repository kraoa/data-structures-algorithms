"""Tests for the Printer driver (must pass out of the box)."""

import unittest
from functools import lru_cache
from printer import Printer


def _brute_strange_printer(s: str) -> int:
    """Memoized recursion — same recurrence, different code path."""
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i > j:
            return 0
        result = dp(i, j - 1) + 1
        for k in range(i, j):
            if s[k] == s[j]:
                result = min(result, dp(i, k) + dp(k + 1, j - 1))
        return result

    return dp(0, len(s) - 1)


class TestPrinter(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Printer.get_test_cases():
            self.assertEqual(tc.expected, _brute_strange_printer(tc.s),
                             f"s={tc.s!r}")

    def test_single_char(self) -> None:
        tc = next(t for t in Printer.get_test_cases() if t.s == "a")
        self.assertEqual(tc.expected, 1)


if __name__ == "__main__":
    unittest.main()
