"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from graph import Graph, Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(g.num_courses, o) for g, o, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_cycle_returns_empty(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_order(2, [(1, 0), (0, 1)]), [])

    # def test_simple_chain(self) -> None:
    #     solver = Solver()
    #     graph = Graph(2, [(1, 0)])
    #     order = solver.find_order(graph.num_courses, graph.prerequisites)
    #     self.assertTrue(graph.is_valid_order(order))

    # def test_diamond(self) -> None:
    #     solver = Solver()
    #     graph = Graph(4, [(1, 0), (2, 0), (3, 1), (3, 2)])
    #     order = solver.find_order(graph.num_courses, graph.prerequisites)
    #     self.assertTrue(graph.is_valid_order(order))


if __name__ == "__main__":
    unittest.main()
