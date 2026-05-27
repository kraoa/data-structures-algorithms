"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from encoding import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.decode_string("3[a]2[bc]"), "aaabcbc")

    # def test_nested(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.decode_string("3[a2[c]]"), "accaccacc")

    # def test_no_encoding(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.decode_string("abc"), "abc")

    # def test_multi_digit_count(self) -> None:
    #     # Multi-digit k like "10[a]" must accumulate digits correctly.
    #     solver = Solver()
    #     self.assertEqual(solver.decode_string("10[a]"), "a" * 10)

    # def test_double_nesting(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.decode_string("2[3[a]]"), "aaaaaa")


if __name__ == "__main__":
    unittest.main()
