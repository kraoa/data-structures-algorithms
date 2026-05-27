"""Tests for Solver."""

import unittest

from solver import Solver


class TestMinPathSumSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        # Uncomment once Solver is implemented:
        # self.assertEqual(solver.min_path_sum([[1,3,1],[1,5,1],[4,2,1]]), 7)

    # def test_two_row_grid(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_path_sum([[1,2,3],[4,5,6]]), 12)

    # def test_single_cell(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_path_sum([[1]]), 1)

    # def test_2x2(self) -> None:
    #     solver = Solver()
    #     # Down then right: 1+1+1=3; right then down: 1+2+1=4. Min is 3.
    #     self.assertEqual(solver.min_path_sum([[1,2],[1,1]]), 3)


if __name__ == "__main__":
    unittest.main()
