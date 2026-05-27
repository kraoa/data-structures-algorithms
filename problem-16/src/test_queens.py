"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from board import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.n, len(sols)) for tc, sols, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_n1(self) -> None:
    #     solver = Solver()
    #     solutions = solver.solve_n_queens(1)
    #     self.assertEqual(solutions, [["Q"]])

    # def test_all_solutions_valid(self) -> None:
    #     solver = Solver()
    #     for n in [1, 4, 5]:
    #         for sol in solver.solve_n_queens(n):
    #             self.assertTrue(Problem.is_valid_solution(sol, n), f"invalid solution for n={n}: {sol}")

    # def test_no_duplicates(self) -> None:
    #     solver = Solver()
    #     solutions = solver.solve_n_queens(4)
    #     self.assertEqual(len(solutions), len({tuple(sol) for sol in solutions}))


if __name__ == "__main__":
    unittest.main()
