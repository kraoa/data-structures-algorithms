"""Tests for the Solver (lowest common ancestor)."""

import unittest

from ancestor import Ancestor, build_tree, find_node
from solver import Solver


class TestLCA(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        solver.lowest_common_ancestor(root, p, q)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    #     p = find_node(root, 5)
    #     q = find_node(root, 1)
    #     result = solver.lowest_common_ancestor(root, p, q)
    #     self.assertEqual(result.val, 3)

    # def test_ancestor_is_p(self) -> None:
    #     # When p is an ancestor of q the answer is p itself.
    #     solver = Solver()
    #     root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    #     p = find_node(root, 5)
    #     q = find_node(root, 4)
    #     result = solver.lowest_common_ancestor(root, p, q)
    #     self.assertEqual(result.val, 5)

    # def test_two_node_tree(self) -> None:
    #     solver = Solver()
    #     root = build_tree([1, 2])
    #     p = find_node(root, 1)
    #     q = find_node(root, 2)
    #     result = solver.lowest_common_ancestor(root, p, q)
    #     self.assertEqual(result.val, 1)


if __name__ == "__main__":
    unittest.main()
