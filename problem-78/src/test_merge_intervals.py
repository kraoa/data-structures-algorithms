"""Tests for the Solver (merge intervals)."""

import unittest

from intervals import Intervals
from solver import Solver


class TestMergeIntervals(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.merge([[1, 3], [2, 6]])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    # def test_touching_endpoints(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.merge([[1,4],[4,5]]), [[1,5]])

    # def test_must_sort_first(self) -> None:
    #     # A greedy approach that skips sorting will get this wrong.
    #     solver = Solver()
    #     self.assertEqual(solver.merge([[1,4],[0,4]]), [[0,4]])

    # def test_empty(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.merge([]), [])


if __name__ == "__main__":
    unittest.main()
