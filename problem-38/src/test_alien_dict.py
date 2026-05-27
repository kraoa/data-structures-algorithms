"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from alphabet import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_simple_two_chars(self) -> None:
    #     solver = Solver()
    #     result = solver.alien_order(["z", "x"])
    #     self.assertTrue(Problem.is_valid_order(result, ["z", "x"]))
    #     self.assertEqual(len(result), 2)

    # def test_impossible_cycle(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.alien_order(["z", "x", "z"]), "")

    # def test_impossible_prefix(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.alien_order(["abc", "ab"]), "")

    # def test_five_char_ordering(self) -> None:
    #     solver = Solver()
    #     result = solver.alien_order(["wrt", "wrf", "er", "ett", "rftt"])
    #     self.assertEqual(len(result), 5)
    #     self.assertTrue(Problem.is_valid_order(result, ["wrt", "wrf", "er", "ett", "rftt"]))


if __name__ == "__main__":
    unittest.main()
