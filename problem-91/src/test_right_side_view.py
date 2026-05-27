"""Tests for Solver."""

import unittest

from view import build_tree
from solver import Solver


class TestRightSideViewSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.right_side_view(build_tree([1, 2, 3, None, 5, None, 4]))
        # Uncomment once Solver is implemented:
        # self.assertEqual(solver.right_side_view(build_tree([1,2,3,None,5,None,4])), [1,3,4])

    # def test_empty_tree(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.right_side_view(None), [])

    # def test_single_node(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.right_side_view(build_tree([1])), [1])

    # def test_left_child_visible_when_no_right(self) -> None:
    #     # Node 4 is only on the left subtree at depth 3; still visible from right.
    #     solver = Solver()
    #     self.assertEqual(solver.right_side_view(build_tree([1,2,3,4])), [1,3,4])


if __name__ == "__main__":
    unittest.main()
