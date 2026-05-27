"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from lists import Problem, from_list, to_list
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.lists, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_empty_input(self) -> None:
    #     solver = Solver()
    #     self.assertIsNone(solver.merge_k_lists([]))

    # def test_single_list(self) -> None:
    #     solver = Solver()
    #     result = solver.merge_k_lists([from_list([1, 2, 3])])
    #     self.assertEqual(to_list(result), [1, 2, 3])

    # def test_result_is_sorted(self) -> None:
    #     solver = Solver()
    #     result = to_list(solver.merge_k_lists([
    #         from_list([1, 4, 5]),
    #         from_list([1, 3, 4]),
    #         from_list([2, 6]),
    #     ]))
    #     self.assertEqual(result, sorted(result), "result is not sorted")
    #     self.assertEqual(len(result), 8, "wrong number of nodes")


if __name__ == "__main__":
    unittest.main()
