"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from matrix import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     grid = [["1","0","1","0","0"],
    #             ["1","0","1","1","1"],
    #             ["1","1","1","1","1"],
    #             ["1","0","0","1","0"]]
    #     self.assertEqual(solver.maximal_square(grid), 4)

    # def test_all_zeros(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_square([["0"]]), 0)

    # def test_full_square(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_square([["1","1"],["1","1"]]), 4)

    # def test_diagonal_ones_not_a_square(self) -> None:
    #     # A diagonal of '1's has no all-1 2×2 square; answer is 1.
    #     solver = Solver()
    #     self.assertEqual(solver.maximal_square([["1","0"],["0","1"]]), 1)


if __name__ == "__main__":
    unittest.main()
