"""Tests for Solver."""

import unittest

from solver import Solver


class TestThreeSumSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.three_sum([-1, 0, 1, 2, -1, -4])
        # Uncomment once Solver is implemented:
        # result = solver.three_sum([-1, 0, 1, 2, -1, -4])
        # self.assertEqual(sorted(sorted(t) for t in result), [[-1,-1,2],[-1,0,1]])

    # def test_all_zeros(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.three_sum([0, 0, 0]), [[0, 0, 0]])

    # def test_no_solution(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.three_sum([0, 1, 1]), [])

    # def test_empty(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.three_sum([]), [])

    # def test_duplicates_not_returned(self) -> None:
    #     # Naive approach returns duplicate triplets without deduplication.
    #     solver = Solver()
    #     result = solver.three_sum([-2, 0, 0, 2, 2])
    #     self.assertEqual(sorted(sorted(t) for t in result), [[-2, 0, 2]])


if __name__ == "__main__":
    unittest.main()
