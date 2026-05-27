"""Tests for the Robbery driver (must pass out of the box)."""

import unittest
from functools import lru_cache
from typing import Optional
from robbery import Robbery, TreeNode, build_tree


def _brute_rob(root: Optional[TreeNode]) -> int:
    """Memoized recursion on node id — same correctness, different code path."""
    memo = {}

    def dp(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        if id(node) in memo:
            return memo[id(node)]
        # rob this node: skip direct children, use grandchildren
        rob_val = node.val
        if node.left:
            rob_val += dp(node.left.left) + dp(node.left.right)
        if node.right:
            rob_val += dp(node.right.left) + dp(node.right.right)
        skip_val = dp(node.left) + dp(node.right)
        result = max(rob_val, skip_val)
        memo[id(node)] = result
        return result

    return dp(root)


class TestRobbery(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Robbery.get_test_cases():
            root = build_tree(list(tc.values))
            self.assertEqual(tc.expected, _brute_rob(root))

    def test_build_tree_structure(self) -> None:
        root = build_tree([3, 2, 3, None, 3, None, 1])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

    def test_build_tree_empty(self) -> None:
        self.assertIsNone(build_tree([]))


if __name__ == "__main__":
    unittest.main()
