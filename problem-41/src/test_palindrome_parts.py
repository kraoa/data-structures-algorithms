"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from cuts import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     result = solver.partition("aab")
    #     normalized = sorted(tuple(p) for p in result)
    #     self.assertIn(("a","a","b"), normalized)
    #     self.assertIn(("aa","b"), normalized)
    #     self.assertEqual(len(result), 2)

    # def test_single_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.partition("a"), [["a"]])

    # def test_all_palindrome(self) -> None:
    #     solver = Solver()
    #     result = solver.partition("aba")
    #     normalized = sorted(tuple(p) for p in result)
    #     self.assertIn(("aba",), normalized)
    #     self.assertIn(("a","b","a"), normalized)

    # def test_every_part_must_be_palindrome(self) -> None:
    #     # "ab" is not a palindrome, so ["ab"] is not a valid partition.
    #     solver = Solver()
    #     result = solver.partition("ab")
    #     for partition in result:
    #         for part in partition:
    #             self.assertEqual(part, part[::-1])


if __name__ == "__main__":
    unittest.main()
