"""Tests for Board. All of this is just boilerplate to make test cases compact and understandable."""

import unittest

from board import Board, Move, GOAL_STATE


class BoardTest(unittest.TestCase):
    """Unit tests for the Board class."""

    def test_is_solved(self) -> None:
        self.assertTrue(Board(GOAL_STATE).is_solved())

    def test_not_solved(self) -> None:
        # blank one step left of its goal position
        self.assertFalse(Board((1, 2, 3, 4, 5, 6, 7, 0, 8)).is_solved())

    def test_valid_moves_corner(self) -> None:
        # blank at top-left: only DOWN and RIGHT are valid
        board = Board((0, 1, 2, 3, 4, 5, 6, 7, 8))
        moves = board.valid_moves()
        self.assertIn(Move.DOWN, moves)
        self.assertIn(Move.RIGHT, moves)
        self.assertNotIn(Move.UP, moves)
        self.assertNotIn(Move.LEFT, moves)

    def test_valid_moves_center(self) -> None:
        # blank at center: all four directions valid
        board = Board((1, 2, 3, 4, 0, 5, 6, 7, 8))
        self.assertEqual(set(board.valid_moves()), {Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT})

    def test_apply_move(self) -> None:
        # blank at (1,1), move UP swaps blank with the tile directly above
        board = Board((1, 2, 3, 4, 0, 5, 6, 7, 8))
        new_board = board.apply_move(Move.UP)
        self.assertEqual(new_board.tiles(), (1, 0, 3, 4, 2, 5, 6, 7, 8))

    def test_apply_move_reaches_goal(self) -> None:
        # blank at (2,1), one RIGHT move solves the puzzle
        board = Board((1, 2, 3, 4, 5, 6, 7, 0, 8))
        solved = board.apply_move(Move.RIGHT)
        self.assertTrue(solved.is_solved())

    def test_move_history(self) -> None:
        board = Board((1, 2, 3, 4, 0, 5, 6, 7, 8))
        board2 = board.apply_move(Move.UP)
        board3 = board2.apply_move(Move.LEFT)
        self.assertEqual(board3.move_history(), [Move.UP, Move.LEFT])

    def test_is_solvable_true(self) -> None:
        self.assertTrue(Board(GOAL_STATE).is_solvable())
        self.assertTrue(Board((1, 2, 3, 4, 5, 6, 7, 0, 8)).is_solvable())

    def test_is_solvable_false(self) -> None:
        # swapping tiles 7 and 8 from goal creates exactly 1 inversion → unsolvable
        self.assertFalse(Board((1, 2, 3, 4, 5, 6, 8, 7, 0)).is_solvable())

    def test_apply_invalid_move_raises(self) -> None:
        board = Board((0, 1, 2, 3, 4, 5, 6, 7, 8))  # blank at top-left
        with self.assertRaises(ValueError):
            board.apply_move(Move.UP)


if __name__ == "__main__":
    unittest.main()
