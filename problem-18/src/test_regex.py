"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from patterns import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.s, tc.p, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_exact_match(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("abc", "abc"))
    #     self.assertFalse(solver.is_match("abc", "ab"))

    # def test_star_zero_times(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("b", "a*b"))  # a* matches ""

    # def test_dot_star(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("anything", ".*"))


if __name__ == "__main__":
    unittest.main()
