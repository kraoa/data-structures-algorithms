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
        # failures = [(tc.grid, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_all_rotten(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.oranges_rotting([[2, 2], [2, 2]]), 0)

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.oranges_rotting([[1]]), -1)

    # def test_one_step(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.oranges_rotting([[2, 1]]), 1)


if __name__ == "__main__":
    unittest.main()
