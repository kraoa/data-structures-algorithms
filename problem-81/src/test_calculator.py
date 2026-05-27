"""Tests for the Calculator driver."""

import unittest

from calculator import Calculator, TestCase


def _eval_reference(s: str) -> int:
    """Use Python's eval to compute the expected result."""
    return int(eval(s))  # noqa: S307 — intentional: only used in tests with known-safe inputs


class TestCalculatorDriver(unittest.TestCase):
    def test_expected_values_match_eval(self) -> None:
        for tc in Calculator.get_test_cases():
            self.assertEqual(
                tc.expected,
                _eval_reference(tc.s),
                msg=f"Mismatch for s={tc.s!r}",
            )

    def test_all_test_cases_have_integer_expected(self) -> None:
        for tc in Calculator.get_test_cases():
            self.assertIsInstance(tc.expected, int)


if __name__ == "__main__":
    unittest.main()
