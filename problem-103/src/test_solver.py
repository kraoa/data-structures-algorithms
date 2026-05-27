"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from collinear import Collinear
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.max_points([[1,1],[2,2],[3,3]])  # must not crash

    # def test_all_collinear(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_points([[1,1],[2,2],[3,3]]), 3)

    # def test_four_collinear(self) -> None:
    #     solver = Solver()
    #     points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    #     self.assertEqual(solver.max_points(points), 4)

    # def test_single_point(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_points([[0,0]]), 1)

    # def test_duplicate_points(self) -> None:
    #     # Duplicate points must count toward the max; slope map alone won't handle this.
    #     solver = Solver()
    #     self.assertEqual(solver.max_points([[0,0],[1,1],[0,0]]), 3)


if __name__ == "__main__":
    unittest.main()
