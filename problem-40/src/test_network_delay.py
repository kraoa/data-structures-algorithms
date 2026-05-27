"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from graph import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)

    # def test_unreachable(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.network_delay_time([[1,2,1]], 2, 2), -1)

    # def test_single_node(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.network_delay_time([], 1, 1), 0)

    # def test_indirect_path_cheaper(self) -> None:
    #     # Direct 1→2 costs 9; via 1→3→2 costs 2. Dijkstra must find the better path.
    #     solver = Solver()
    #     self.assertEqual(solver.network_delay_time([[1,2,9],[1,3,1],[3,2,1]], 3, 1), 2)


if __name__ == "__main__":
    unittest.main()
