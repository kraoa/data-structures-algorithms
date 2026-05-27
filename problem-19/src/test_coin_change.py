"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from coins import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.coins, tc.amount, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_zero_amount(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.coin_change([1, 5], 0), 0)

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.coin_change([2], 3), -1)

    # def test_greedy_counterexample(self) -> None:
    #     # Greedy would pick 11, then 1+1+1+1 = 5 coins total.
    #     # Optimal is 5+5+5 = 3 coins.
    #     solver = Solver()
    #     self.assertEqual(solver.coin_change([1, 5, 11], 15), 3)


if __name__ == "__main__":
    unittest.main()
