"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from scheduling import Scheduling
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]])  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]]), 3)

    # def test_impossible(self) -> None:
    #     # Both courses are infeasible together; greedy must recognize this.
    #     solver = Solver()
    #     self.assertEqual(solver.schedule_course([[3,2],[4,3]]), 0)

    # def test_swap_needed(self) -> None:
    #     # Greedy without swapping would take [5,5] then fail to fit [4,6] and [2,6].
    #     solver = Solver()
    #     self.assertEqual(solver.schedule_course([[5,5],[4,6],[2,6]]), 2)

    # def test_single_course(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.schedule_course([[1,2]]), 1)


if __name__ == "__main__":
    unittest.main()
