"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from tasks import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.least_interval(["A","A","A","B","B","B"], 2), 8)

    # def test_no_cooldown(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.least_interval(["A","A","A","B","B","B"], 0), 6)

    # def test_single_task(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.least_interval(["A"], 2), 1)

    # def test_dense_schedule_no_idle(self) -> None:
    #     # Many distinct tasks fill every slot with no idle needed.
    #     solver = Solver()
    #     self.assertEqual(solver.least_interval(["A","C","A","B","D","B"], 1), 6)


if __name__ == "__main__":
    unittest.main()
