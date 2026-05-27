"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from combinations import Problem
from solver import Solver


class TestComboSum(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.combination_sum([2, 3, 6, 7], 7)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     result = sorted(sorted(c) for c in solver.combination_sum([2, 3, 6, 7], 7))
    #     self.assertEqual(result, [[2, 2, 3], [7]])

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.combination_sum([2], 1), [])

    # def test_repeated_use(self) -> None:
    #     # Candidate 1 must be used multiple times to reach target 3.
    #     solver = Solver()
    #     result = sorted(sorted(c) for c in solver.combination_sum([1], 3))
    #     self.assertEqual(result, [[1, 1, 1]])


if __name__ == "__main__":
    unittest.main()
