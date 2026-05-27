"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from ordering import Ordering
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.largest_number([10, 2])  # must not crash

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.largest_number([10, 2]), "210")

    # def test_multiple_numbers(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.largest_number([3, 30, 34, 5, 9]), "9534330")

    # def test_all_zeros(self) -> None:
    #     # Must return "0" not "00".
    #     solver = Solver()
    #     self.assertEqual(solver.largest_number([0, 0]), "0")

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.largest_number([1]), "1")


if __name__ == "__main__":
    unittest.main()
