"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from frequency import Problem
from solver import Solver


class TestTopK(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.top_k_frequent([1, 1, 1, 2, 2, 3], 2)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(sorted(solver.top_k_frequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.top_k_frequent([1], 1), [1])

    # def test_negative_elements(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(sorted(solver.top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)), [-1, 2])


if __name__ == "__main__":
    unittest.main()
