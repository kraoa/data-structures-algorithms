"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from stations import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]), 3)

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.can_complete_circuit([2,3,4], [3,4,3]), -1)

    # def test_single_station(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.can_complete_circuit([5], [4]), 0)

    # def test_greedy_counterexample(self) -> None:
    #     # Starting at 0: tank goes negative after 2 steps.
    #     # A naive approach might restart at 1, but 1 also fails; correct answer is 1.
    #     solver = Solver()
    #     self.assertEqual(solver.can_complete_circuit([1, 2], [2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
