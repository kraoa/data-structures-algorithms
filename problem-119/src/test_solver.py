"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from stations import Problem
from solver import Solver


class TestNearestStationSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_basic_nearest(self) -> None:
    #     solver = Solver()
    #     result = solver.nearest_station([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]], [[9, 2]])
    #     self.assertEqual(result, [[8, 1]])

    # def test_single_station(self) -> None:
    #     solver = Solver()
    #     result = solver.nearest_station([[1, 2]], [[5, 5]])
    #     self.assertEqual(result, [[1, 2]])

    # def test_tie_breaking_by_index(self) -> None:
    #     # [1,0] and [0,1] are both at dist²=5 from [2,2]; smaller index wins.
    #     solver = Solver()
    #     result = solver.nearest_station([[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]], [[2, 2]])
    #     self.assertEqual(result, [[1, 0]])


if __name__ == "__main__":
    unittest.main()
