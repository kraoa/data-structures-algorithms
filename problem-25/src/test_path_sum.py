"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from tree import Problem, from_list
from solver import Solver


class TestPathSum(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.max_path_sum(from_list([1, 2, 3]))

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_path_sum(from_list([1, 2, 3])), 6)

    # def test_all_negative(self) -> None:
    #     # Must return the least-negative single node, not 0.
    #     solver = Solver()
    #     self.assertEqual(solver.max_path_sum(from_list([-3])), -3)

    # def test_negative_children_skipped(self) -> None:
    #     # Including a negative child reduces the path sum.
    #     solver = Solver()
    #     self.assertEqual(solver.max_path_sum(from_list([2, -1, None])), 2)


if __name__ == "__main__":
    unittest.main()
