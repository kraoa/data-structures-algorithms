"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest

from puzzle import Puzzle
from solver import Solver


class SolverTest(unittest.TestCase):
    """Unit tests for the Solver class."""

    def test_should_solve_known_case(self) -> None:
        """Test that the solver can solve a fixed puzzle."""
        puzzle = Puzzle("1234")
        solver = Solver(puzzle)
        solver.solve_puzzle()
        # Uncomment these assertions once Solver is implemented:
        # self.assertTrue(puzzle.won(), "couldn't solve '1234'")
        # self.assertEqual(
        #     len(solver.get_guesses()),
        #     puzzle.num_guesses(),
        #     "don't cheat!",
        # )
        # self.assertLessEqual(puzzle.num_guesses(), 10, "too many guesses")

    # def test_should_be_optimal(self) -> None:
    #     """Knuth's algorithm solves any 4-peg 6-color code in at most 5 guesses."""
    #     import random
    #     random.seed(42)
    #     worst = 0
    #     for _ in range(200):
    #         puzzle = Puzzle()
    #         solver = Solver(puzzle)
    #         solver.solve_puzzle()
    #         worst = max(worst, puzzle.num_guesses())
    #     self.assertLessEqual(worst, 5, f"worst case was {worst} guesses, expected <= 5")


if __name__ == "__main__":
    unittest.main()
