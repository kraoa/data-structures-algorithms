"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from splits import Problem
from solver import Solver


class TestSplitArraySolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_two_subarrays(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.split_array([7, 2, 5, 10, 8], 2), 18)

    # def test_single_subarray(self) -> None:
    #     # k=1 forces the whole array into one subarray; answer is its sum.
    #     solver = Solver()
    #     self.assertEqual(solver.split_array([1, 2, 3, 4, 5], 1), 15)

    # def test_k_equals_len(self) -> None:
    #     # Each element is its own subarray; answer is the maximum element.
    #     solver = Solver()
    #     self.assertEqual(solver.split_array([1, 4, 4], 3), 4)


if __name__ == "__main__":
    unittest.main()
