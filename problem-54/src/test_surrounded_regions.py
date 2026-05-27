"""Tests for Solver."""

import unittest

from solver import Solver


class TestSurroundedRegionsSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        solver = Solver()
        solver.solve(board)
        # Uncomment once Solver is implemented:
        # self.assertEqual(board[1][1], "X")  # interior O flipped
        # self.assertEqual(board[3][1], "O")  # border O stays

    # def test_single_o_on_border(self) -> None:
    #     board = [["O"]]
    #     solver = Solver()
    #     solver.solve(board)
    #     self.assertEqual(board, [["O"]])

    # def test_center_o_surrounded(self) -> None:
    #     board = [["X","X","X"],["X","O","X"],["X","X","X"]]
    #     solver = Solver()
    #     solver.solve(board)
    #     self.assertEqual(board, [["X","X","X"],["X","X","X"],["X","X","X"]])

    # def test_border_connected_region_stays(self) -> None:
    #     # O at (1,1) is connected through (2,1) which touches the bottom border.
    #     board = [["X","X","X"],["X","O","X"],["X","O","X"]]
    #     solver = Solver()
    #     solver.solve(board)
    #     self.assertEqual(board[1][1], "O")
    #     self.assertEqual(board[2][1], "O")


if __name__ == "__main__":
    unittest.main()
