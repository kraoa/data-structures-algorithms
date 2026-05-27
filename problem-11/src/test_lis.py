"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from sequences import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.nums, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.length_of_lis([42]), 1)

    # def test_strictly_increasing(self) -> None:
    #     solver = Solver()
    #     # Duplicates must not count — LIS is strictly increasing.
    #     self.assertEqual(solver.length_of_lis([1, 1, 1]), 1)
    #     self.assertEqual(solver.length_of_lis([1, 2, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()
