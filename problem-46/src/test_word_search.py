"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from grid import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_found(self) -> None:
    #     solver = Solver()
    #     board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #     self.assertTrue(solver.exist(board, "ABCCED"))

    # def test_not_found(self) -> None:
    #     solver = Solver()
    #     board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #     self.assertFalse(solver.exist(board, "ABCB"))

    # def test_no_revisit(self) -> None:
    #     # The path must not revisit the same cell.
    #     solver = Solver()
    #     self.assertFalse(solver.exist([["a","b"],["c","d"]], "abcd"))

    # def test_single_cell(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.exist([["a"]], "a"))
    #     self.assertFalse(solver.exist([["a"]], "b"))


if __name__ == "__main__":
    unittest.main()
