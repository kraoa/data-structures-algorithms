"""Tests for Solver."""

import unittest

from solver import Solver


class TestCountSmallerSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.count_smaller([5, 2, 6, 1])
        # Uncomment once Solver is implemented:
        # self.assertEqual(solver.count_smaller([5,2,6,1]), [2,1,1,0])

    # def test_negative_numbers(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_smaller([-1, -1]), [0, 0])

    # def test_fully_descending(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_smaller([5,4,3,2,1]), [4,3,2,1,0])

    # def test_fully_ascending(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_smaller([1,2,3,4,5]), [0,0,0,0,0])

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_smaller([1]), [0])


if __name__ == "__main__":
    unittest.main()
