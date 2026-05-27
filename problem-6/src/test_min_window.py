"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from window import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.s, tc.t, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_no_window(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_window("a", "b"), "")

    # def test_t_longer_than_s(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_window("ab", "abc"), "")

    # def test_exact_window(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_window("abc", "abc"), "abc")


if __name__ == "__main__":
    unittest.main()
