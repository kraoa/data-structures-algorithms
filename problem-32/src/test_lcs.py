"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from subsequences import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.lcs("abcde", "ace"), 3)

    # def test_identical_strings(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.lcs("abc", "abc"), 3)

    # def test_no_common(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.lcs("abc", "def"), 0)

    # def test_empty_string(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.lcs("", "abc"), 0)

    # def test_order_matters(self) -> None:
    #     # "ba" is NOT a subsequence of "abc" in order, but "ab" is — result is 2, not 3.
    #     solver = Solver()
    #     self.assertEqual(solver.lcs("abc", "cab"), 2)


if __name__ == "__main__":
    unittest.main()
