"""Tests for the Problem driver (shipping.py)."""

import unittest
from shipping import Problem


class TestShipping(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.weights, tc.days),
                msg=f"weights={tc.weights} days={tc.days}",
            )

    def test_single_package(self) -> None:
        self.assertEqual(Problem.brute_force([10], 1), 10)

    def test_exact_capacity(self) -> None:
        # Each package needs its own day at minimum capacity = max.
        self.assertEqual(Problem.brute_force([5, 5, 5], 3), 5)

    def test_feasible_checks_monotone(self) -> None:
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(Problem._feasible(weights, 5, 15))
        self.assertFalse(Problem._feasible(weights, 5, 14))


if __name__ == "__main__":
    unittest.main()
