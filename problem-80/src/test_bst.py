"""Tests for the BST driver."""

import unittest
from typing import List, Optional

from bst import BST, TestCase, TreeNode, build_tree


def _inorder(root: Optional[TreeNode]) -> List[int]:
    """Return in-order traversal values."""
    result: List[int] = []
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result


def _brute_force_is_valid(values: List[Optional[int]]) -> bool:
    """In-order traversal must be strictly increasing for a valid BST."""
    root = build_tree(values)
    vals = _inorder(root)
    return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))


class TestBSTDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in BST.get_test_cases():
            result = _brute_force_is_valid(tc.values)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for values={tc.values}",
            )

    def test_build_tree_with_none_gaps(self) -> None:
        root = build_tree([5, 4, 6, None, None, 3, 7])
        self.assertEqual(root.val, 5)
        self.assertEqual(root.left.val, 4)
        self.assertEqual(root.right.val, 6)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 3)
        self.assertEqual(root.right.right.val, 7)


if __name__ == "__main__":
    unittest.main()
