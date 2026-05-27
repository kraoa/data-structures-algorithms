"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from partitions import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.can_partition([1, 5, 11, 5]))

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.can_partition([1, 2, 3, 5]))

    # def test_odd_total(self) -> None:
    #     # Odd total means no equal split is possible — no need to search.
    #     solver = Solver()
    #     self.assertFalse(solver.can_partition([1]))

    # def test_large_values(self) -> None:
    #     # Subset sum DP must handle large values efficiently.
    #     solver = Solver()
    #     self.assertFalse(solver.can_partition([1, 2, 5]))


if __name__ == "__main__":
    unittest.main()
