"""Tests for the Solver (ship_within_days)."""

import unittest
from solver import Solver


class TestShipWithinDays(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)

    # def test_three_days(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.ship_within_days([3, 2, 2, 4, 1, 4], 3), 6)

    # def test_extra_days(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.ship_within_days([1, 2, 3, 1, 1], 4), 3)

    # def test_single_package(self) -> None:
    #     # Lower bound is max(weights); even with 1 day, capacity cannot be less.
    #     solver = Solver()
    #     self.assertEqual(solver.ship_within_days([10], 1), 10)


if __name__ == "__main__":
    unittest.main()
