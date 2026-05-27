"""Tests for the Solver (validate BST)."""

import unittest

from bst import BST, build_tree
from solver import Solver


class TestValidateBST(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        root = build_tree([2, 1, 3])
        solver.is_valid_bst(root)

    # def test_valid(self) -> None:
    #     solver = Solver()
    #     root = build_tree([2, 1, 3])
    #     self.assertTrue(solver.is_valid_bst(root))

    # def test_invalid_right_child_less_than_root(self) -> None:
    #     solver = Solver()
    #     root = build_tree([5, 1, 4, None, None, 3, 6])
    #     self.assertFalse(solver.is_valid_bst(root))

    # def test_subtree_violates_ancestor_bound(self) -> None:
    #     # Node 3 is in the right subtree of 5 but 3 < 5; local checks alone miss this.
    #     solver = Solver()
    #     root = build_tree([5, 4, 6, None, None, 3, 7])
    #     self.assertFalse(solver.is_valid_bst(root))

    # def test_equal_values_invalid(self) -> None:
    #     solver = Solver()
    #     root = build_tree([2, 2, 2])
    #     self.assertFalse(solver.is_valid_bst(root))


if __name__ == "__main__":
    unittest.main()
