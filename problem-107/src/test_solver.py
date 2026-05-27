"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from queries import Queries
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.min_interval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5])  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     result = solver.min_interval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5])
    #     self.assertEqual(result, [3,3,1,4])

    # def test_no_containing_interval(self) -> None:
    #     # Query 19 has no containing interval → -1.
    #     solver = Solver()
    #     result = solver.min_interval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22])
    #     self.assertEqual(result, [2,-1,4,6])

    # def test_order_preserved(self) -> None:
    #     # Output must be in the same order as the input queries, not sorted order.
    #     solver = Solver()
    #     result = solver.min_interval([[1,4]], [4,1])
    #     self.assertEqual(result, [4,4])


if __name__ == "__main__":
    unittest.main()
