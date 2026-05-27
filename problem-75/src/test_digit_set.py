"""Tests for the digit_set driver. Must pass out of the box."""

import unittest
from typing import List

from digit_set import Problem, TestCase


def _brute_force(digits: List[str], n: int) -> int:
    """Count integers in [1, n] whose every digit belongs to the digit set."""
    digit_set = set(digits)
    return sum(
        1 for i in range(1, n + 1) if all(c in digit_set for c in str(i))
    )


class TestDigitSetDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            # Brute force is only feasible for small n.
            if tc.n > 100_000:
                continue
            bf = _brute_force(tc.digits, tc.n)
            self.assertEqual(
                tc.expected,
                bf,
                msg=f"digits={tc.digits}, n={tc.n}: stored={tc.expected}, brute force={bf}",
            )

    def test_run_returns_correct_structure(self) -> None:
        class _ZeroSolver:
            def at_most_n_given_digit_set(self, digits, n):
                return 0

        results = Problem.run(_ZeroSolver())
        self.assertEqual(len(results), len(Problem.get_test_cases()))
        for tc, actual, passed in results:
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
