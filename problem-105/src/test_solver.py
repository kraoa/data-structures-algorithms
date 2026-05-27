"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from range_count import RangeCount
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.count_range_sum([-2, 5, -1], -2, 2)  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_range_sum([-2, 5, -1], -2, 2), 3)

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_range_sum([0], 0, 0), 1)

    # def test_multiple_valid_ranges(self) -> None:
    #     # [1,2,3] with [0,3]: sums 1,2,3,3 are valid (not 5,6).
    #     solver = Solver()
    #     self.assertEqual(solver.count_range_sum([1, 2, 3], 0, 3), 4)

    # def test_negative_single(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_range_sum([-1], -1, 0), 1)


if __name__ == "__main__":
    unittest.main()
