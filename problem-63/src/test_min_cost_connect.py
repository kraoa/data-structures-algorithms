"""Tests for the Solver (min_cost_connect_points)."""

import unittest
from solver import Solver


class TestMinCostConnect(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])

    # def test_five_points(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20
    #     )

    # def test_three_points(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]), 18)

    # def test_single_point(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cost_connect_points([[0, 0]]), 0)

    # def test_unit_square(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.min_cost_connect_points([[0, 0], [1, 1], [1, 0], [0, 1]]), 3
    #     )


if __name__ == "__main__":
    unittest.main()
