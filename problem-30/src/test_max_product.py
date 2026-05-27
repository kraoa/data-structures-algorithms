"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from subarray import Problem
from solver import Solver


class TestMaxProduct(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.max_product([2, 3, -2, 4])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_product([2, 3, -2, 4]), 6)

    # def test_all_negative_even_count(self) -> None:
    #     # Two negatives multiply to a large positive.
    #     solver = Solver()
    #     self.assertEqual(solver.max_product([-2, 3, -4]), 24)

    # def test_zero_resets_product(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_product([-2, 0, -1]), 0)

    # def test_single_negative(self) -> None:
    #     # Must return the element itself, not 0.
    #     solver = Solver()
    #     self.assertEqual(solver.max_product([-1]), -1)


if __name__ == "__main__":
    unittest.main()
