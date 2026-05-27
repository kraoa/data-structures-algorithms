"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest

from board import Board, Move, GOAL_STATE
from solver import Solver


class SolverTest(unittest.TestCase):
    """Unit tests for the Solver class."""

    def test_already_solved(self) -> None:
        """Solver should handle an already-solved board."""
        board = Board(GOAL_STATE)
        solver = Solver(board)
        solver.solve()
        # Uncomment these assertions once Solver is implemented:
        # solution = solver.get_solution()
        # self.assertIsNotNone(solution)
        # self.assertEqual(len(solution), 0)

    def test_one_move(self) -> None:
        """Solver should solve a board that's one move from the goal."""
        board = Board((1, 2, 3, 4, 5, 6, 7, 0, 8))
        solver = Solver(board)
        solver.solve()
        # Uncomment these assertions once Solver is implemented:
        # solution = solver.get_solution()
        # self.assertIsNotNone(solution)
        # self.assertEqual(len(solution), 1)
        # self.assertEqual(solution[0], Move.RIGHT)

    # def test_optimal_solution(self) -> None:
    #     """A* with Manhattan distance heuristic should find the shortest path."""
    #     board = Board((1, 2, 3, 0, 4, 6, 7, 5, 8))
    #     solver = Solver(board)
    #     solver.solve()
    #     solution = solver.get_solution()
    #     self.assertIsNotNone(solution)
    #     # verify the solution actually reaches the goal
    #     state = board
    #     for move in solution:
    #         state = state.apply_move(move)
    #     self.assertTrue(state.is_solved())

    # def test_unsolvable(self) -> None:
    #     """Solver should return None for an unsolvable configuration."""
    #     board = Board((1, 2, 3, 4, 5, 6, 8, 7, 0))
    #     solver = Solver(board)
    #     solver.solve()
    #     self.assertIsNone(solver.get_solution())


if __name__ == "__main__":
    unittest.main()
