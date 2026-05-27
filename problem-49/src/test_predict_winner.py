"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from game import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_player2_wins(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.predict_the_winner([1, 5, 2]))

    # def test_player1_wins(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.predict_the_winner([1, 5, 233, 7]))

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.predict_the_winner([1]))

    # def test_tie_counts_as_win(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.predict_the_winner([0, 0]))

    # def test_greedy_fails(self) -> None:
    #     # Greedy (always pick the larger end) would take 5 first from [1,5,2].
    #     # But that still loses. The minimax DP is needed to prove it.
    #     solver = Solver()
    #     self.assertFalse(solver.predict_the_winner([1, 5, 2]))


if __name__ == "__main__":
    unittest.main()
