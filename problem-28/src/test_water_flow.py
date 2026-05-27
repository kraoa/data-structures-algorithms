"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from grid import Problem
from solver import Solver


class TestWaterFlow(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.pacific_atlantic([[1, 2, 2, 3, 5],
                                 [3, 2, 3, 4, 4],
                                 [2, 4, 5, 3, 1],
                                 [6, 7, 1, 4, 5],
                                 [5, 1, 1, 2, 4]])

    # def test_single_cell(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.pacific_atlantic([[1]]), [[0, 0]])

    # def test_all_same_height(self) -> None:
    #     solver = Solver()
    #     result = sorted(solver.pacific_atlantic([[1, 1], [1, 1]]))
    #     self.assertEqual(result, [[0, 0], [0, 1], [1, 0], [1, 1]])

    # def test_leetcode_example(self) -> None:
    #     solver = Solver()
    #     heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    #     result = sorted(solver.pacific_atlantic(heights))
    #     self.assertEqual(result, [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])


if __name__ == "__main__":
    unittest.main()
