import unittest

from board import Board
from solver import Solver


class TestMinesweeper(unittest.TestCase):
    def test_runs_without_crash(self) -> None:
        solver = Solver()
        Board.run(solver)

    # def test_click_mine(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.update([["M"]], (0, 0)), [["X"]])

    # def test_single_empty_cell(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.update([["E"]], (0, 0)), [["B"]])

    # def test_flood_fill_cascades(self) -> None:
    #     # Clicking far from the mine triggers a blank-flood that stops at mine borders.
    #     board = [
    #         ["E", "E", "E", "E", "E"],
    #         ["E", "E", "M", "E", "E"],
    #         ["E", "E", "E", "E", "E"],
    #         ["E", "E", "E", "E", "E"],
    #     ]
    #     expected = [
    #         ["B", "1", "E", "1", "B"],
    #         ["B", "1", "M", "1", "B"],
    #         ["B", "1", "1", "1", "B"],
    #         ["B", "B", "B", "B", "B"],
    #     ]
    #     solver = Solver()
    #     self.assertEqual(solver.update(board, (3, 0)), expected)

    # def test_adjacent_mine_reveals_digit_only(self) -> None:
    #     # A cell next to a mine gets a digit; its 'E' neighbors are NOT revealed.
    #     solver = Solver()
    #     result = solver.update([["E", "M"], ["E", "E"]], (1, 1))
    #     self.assertEqual(result, [["E", "M"], ["E", "1"]])


if __name__ == "__main__":
    unittest.main()
