"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from flights import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    #     self.assertEqual(solver.find_cheapest_price(4, flights, 0, 3, 1), 700)

    # def test_direct_only_when_k_zero(self) -> None:
    #     solver = Solver()
    #     flights = [[0,1,100],[1,2,100],[0,2,500]]
    #     self.assertEqual(solver.find_cheapest_price(3, flights, 0, 2, 0), 500)

    # def test_unreachable(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_cheapest_price(3, [[0,1,100],[1,2,100]], 0, 2, 0), -1)

    # def test_round_trip_not_exploited(self) -> None:
    #     # A cycle 0→1→2→0 must not be used to reduce costs via extra hops.
    #     # k=1 means exactly 1 intermediate stop; best route is 0→1→3 = 700.
    #     solver = Solver()
    #     flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    #     self.assertEqual(solver.find_cheapest_price(4, flights, 0, 3, 1), 700)


if __name__ == "__main__":
    unittest.main()
