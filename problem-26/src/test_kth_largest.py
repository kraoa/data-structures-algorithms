"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from selection import Problem
from solver import Solver


class TestKthLargest(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.find_kth_largest([3, 2, 1, 5, 6, 4], 2)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_largest([1], 1), 1)

    # def test_duplicates(self) -> None:
    #     # k=4 in [3,2,3,1,2,4,5,5,6]: sorted desc → [6,5,5,4,...], so answer is 4.
    #     solver = Solver()
    #     self.assertEqual(solver.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == "__main__":
    unittest.main()
