"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from overlap import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]), 1)

    # def test_all_same(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.erase_overlap_intervals([[1,2],[1,2],[1,2]]), 2)

    # def test_no_overlap(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.erase_overlap_intervals([[1,2],[2,3]]), 0)

    # def test_sort_by_end_not_start(self) -> None:
    #     # Sorting by start would keep [1,100] first, forcing removal of 3 others.
    #     # Sorting by end correctly removes only 2.
    #     solver = Solver()
    #     self.assertEqual(solver.erase_overlap_intervals([[1,100],[11,22],[1,11],[2,12]]), 2)


if __name__ == "__main__":
    unittest.main()
