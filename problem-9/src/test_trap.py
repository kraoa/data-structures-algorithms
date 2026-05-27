"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from elevation import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.height, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_no_water(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.trap([1, 2, 3]), 0)  # ascending — no water
    #     self.assertEqual(solver.trap([3, 2, 1]), 0)  # descending — no water

    # def test_single_valley(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.trap([3, 0, 3]), 3)

    # def test_does_not_mutate_input(self) -> None:
    #     solver = Solver()
    #     height = [4, 2, 0, 3, 2, 5]
    #     original = list(height)
    #     solver.trap(height)
    #     self.assertEqual(height, original, "solver must not modify the input list")


if __name__ == "__main__":
    unittest.main()
