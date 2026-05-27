"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from window import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_sliding_window([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

    # def test_k_equals_one(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_sliding_window([1,-1], 1), [1,-1])

    # def test_decreasing_sequence(self) -> None:
    #     # The window max is always the leftmost element.
    #     solver = Solver()
    #     self.assertEqual(solver.max_sliding_window([5,4,3,2,1], 3), [5,4,3])

    # def test_deque_correctness(self) -> None:
    #     # A naive approach that just tracks a running max fails when the max scrolls out.
    #     solver = Solver()
    #     self.assertEqual(solver.max_sliding_window([5,1,1,1,5], 3), [5,1,5])


if __name__ == "__main__":
    unittest.main()
