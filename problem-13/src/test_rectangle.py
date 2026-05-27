"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from histogram import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.heights, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_single_bar(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.largest_rectangle([5]), 5)

    # def test_all_same_height(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.largest_rectangle([3, 3, 3]), 9)

    # def test_valley(self) -> None:
    #     solver = Solver()
    #     # A valley forces you to use only the valley's height across the full width.
    #     self.assertEqual(solver.largest_rectangle([5, 1, 5]), 5)


if __name__ == "__main__":
    unittest.main()
