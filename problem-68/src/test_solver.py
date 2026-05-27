"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from reachability import Problem
from solver import Solver


class TestShortestPathSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_star_graph(self) -> None:
    #     # One center node connected to three leaves; must backtrack through center.
    #     solver = Solver()
    #     self.assertEqual(solver.shortest_path_length([[1, 2, 3], [0], [0], [0]]), 4)

    # def test_two_nodes(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.shortest_path_length([[1], [0]]), 1)

    # def test_triangle(self) -> None:
    #     # All nodes reachable in 2 hops from any starting vertex.
    #     solver = Solver()
    #     self.assertEqual(solver.shortest_path_length([[1, 2], [0, 2], [0, 1]]), 2)


if __name__ == "__main__":
    unittest.main()
