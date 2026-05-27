"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from multiplication import Problem
from solver import Solver


class TestMultiplicationSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_3x3_k5(self) -> None:
    #     # Sorted 3x3 table: 1,2,2,3,3,4,6,6,9 — 5th element is 3.
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_number(3, 3, 5), 3)

    # def test_2x3_k6(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_number(2, 3, 6), 6)

    # def test_k_equals_one(self) -> None:
    #     # Smallest entry in any m x n table is always 1*1 = 1.
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_number(9, 9, 1), 1)


if __name__ == "__main__":
    unittest.main()
