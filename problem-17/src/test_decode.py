"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from decodings import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.s, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_zero_ways(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_decodings("0"), 0)
    #     self.assertEqual(solver.num_decodings("06"), 0)

    # def test_single_digit(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_decodings("1"), 1)


if __name__ == "__main__":
    unittest.main()
