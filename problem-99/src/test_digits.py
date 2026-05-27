"""Tests for the Digits driver (must pass out of the box)."""

import unittest
from digits import Digits


def _brute_count(n: int) -> int:
    return sum(str(i).count('1') for i in range(1, n + 1))


class TestDigits(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Digits.get_test_cases():
            if tc.n > 100_000:
                continue
            self.assertEqual(tc.expected, _brute_count(tc.n),
                             f"n={tc.n}")

    def test_zero(self) -> None:
        tc = next(t for t in Digits.get_test_cases() if t.n == 0)
        self.assertEqual(tc.expected, 0)


if __name__ == "__main__":
    unittest.main()
