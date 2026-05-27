"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from digit_set import Problem
from solver import Solver


class TestDigitSetSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_four_digit_set_under_100(self) -> None:
    #     # 4 one-digit numbers + 4*4=16 two-digit numbers; no valid three-digit number <= 100.
    #     solver = Solver()
    #     self.assertEqual(solver.at_most_n_given_digit_set(["1", "3", "5", "7"], 100), 20)

    # def test_single_digit_n(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.at_most_n_given_digit_set(["1", "4", "9"], 8), 2)

    # def test_n_not_in_digit_set(self) -> None:
    #     # n itself (25) cannot be formed; only {1,2,11,12,21,22} qualify.
    #     solver = Solver()
    #     self.assertEqual(solver.at_most_n_given_digit_set(["1", "2"], 25), 6)


if __name__ == "__main__":
    unittest.main()
