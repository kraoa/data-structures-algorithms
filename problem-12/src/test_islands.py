"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from grid import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(len(tc.grid), actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_does_not_count_diagonal(self) -> None:
    #     solver = Solver()
    #     grid = [["1","0"],["0","1"]]
    #     self.assertEqual(solver.num_islands(grid), 2)

    # def test_all_water(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_islands([["0"]]), 0)


if __name__ == "__main__":
    unittest.main()
