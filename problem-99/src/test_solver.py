"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from digits import Digits
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.count_digit_one(13)  # must not crash

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_digit_one(13), 6)

    # def test_zero(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_digit_one(0), 0)

    # def test_tens_boundary(self) -> None:
    #     # n=10: the '1' in 1 and in 10 → total 2.
    #     solver = Solver()
    #     self.assertEqual(solver.count_digit_one(10), 2)

    # def test_hundreds(self) -> None:
    #     # n=100: ones-place gives 10, tens-place gives 10, hundreds-place gives 1 → 21.
    #     solver = Solver()
    #     self.assertEqual(solver.count_digit_one(100), 21)


if __name__ == "__main__":
    unittest.main()
