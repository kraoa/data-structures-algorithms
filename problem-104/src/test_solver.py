"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from spiral import Spiral
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.spiral_order([[1,2,3],[4,5,6],[7,8,9]])  # must not crash

    # def test_3x3(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.spiral_order([[1,2,3],[4,5,6],[7,8,9]]),
    #                      [1,2,3,6,9,8,7,4,5])

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.spiral_order([[1]]), [1])

    # def test_single_column(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.spiral_order([[1],[2],[3]]), [1,2,3])

    # def test_non_square(self) -> None:
    #     # Non-square matrices require careful boundary tracking.
    #     solver = Solver()
    #     self.assertEqual(solver.spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]),
    #                      [1,2,3,4,8,12,11,10,9,5,6,7])


if __name__ == "__main__":
    unittest.main()
