"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from rectangle import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     matrix = [["1","0","1","0","0"],
    #               ["1","0","1","1","1"],
    #               ["1","1","1","1","1"],
    #               ["1","0","0","1","0"]]
    #     self.assertEqual(solver.maximal_rectangle(matrix), 6)

    # def test_all_zeros(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_rectangle([["0"]]), 0)

    # def test_full_matrix(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_rectangle([["1","1"],["1","1"]]), 4)

    # def test_histogram_technique(self) -> None:
    #     # The best rectangle spans two rows, which a single-row scan misses.
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_rectangle([["1","0","1"],["1","1","1"]]), 3)


if __name__ == "__main__":
    unittest.main()
