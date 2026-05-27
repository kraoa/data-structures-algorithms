"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from strings import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.word1, tc.word2, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_empty_strings(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_distance("", ""), 0)
    #     self.assertEqual(solver.min_distance("a", ""), 1)
    #     self.assertEqual(solver.min_distance("", "a"), 1)

    # def test_symmetric(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.min_distance("horse", "ros"),
    #         solver.min_distance("ros", "horse"),
    #     )


if __name__ == "__main__":
    unittest.main()
