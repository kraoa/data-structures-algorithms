"""Tests for the Ancestor driver."""

import unittest
from typing import List, Optional

from ancestor import Ancestor, TestCase, TreeNode, build_tree, find_node


def _path_to(root: Optional[TreeNode], target: int) -> Optional[List[int]]:
    """Return list of node values from root to target, or None if not found."""
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    for child in (root.left, root.right):
        path = _path_to(child, target)
        if path is not None:
            return [root.val] + path
    return None


def _brute_force_lca(values: List[Optional[int]], p: int, q: int) -> Optional[int]:
    """Find LCA value by intersecting root-to-node paths."""
    root = build_tree(values)
    path_p = _path_to(root, p) or []
    path_q = _path_to(root, q) or []
    lca_val = None
    for vp, vq in zip(path_p, path_q):
        if vp == vq:
            lca_val = vp
        else:
            break
    return lca_val


class TestAncestorDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Ancestor.get_test_cases():
            expected_brute = _brute_force_lca(tc.values, tc.p, tc.q)
            self.assertEqual(
                tc.expected,
                expected_brute,
                msg=f"Mismatch for p={tc.p}, q={tc.q} in tree {tc.values}",
            )

    def test_build_tree_bfs_order(self) -> None:
        root = build_tree([1, 2, 3])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

    def test_find_node(self) -> None:
        root = build_tree([3, 5, 1])
        node = find_node(root, 5)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 5)


if __name__ == "__main__":
    unittest.main()
