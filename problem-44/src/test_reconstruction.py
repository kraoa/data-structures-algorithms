"""Tests for Problem. Verifies traversal helpers and stored test-case consistency."""

import unittest
from reconstruction import Problem


class ProblemTest(unittest.TestCase):

    def test_traversals_consistent_with_level_order(self) -> None:
        """Build each reference tree from level_order; check pre/in-order match stored values."""
        for tc in Problem.get_test_cases():
            root = Problem.build_from_level(tc.level_order)
            self.assertEqual(Problem.preorder_of(root), tc.preorder,
                             f"preorder mismatch for level_order={tc.level_order}")
            self.assertEqual(Problem.inorder_of(root), tc.inorder,
                             f"inorder mismatch for level_order={tc.level_order}")

    def test_preorder_single_node(self) -> None:
        root = Problem.build_from_level([42])
        self.assertEqual(Problem.preorder_of(root), [42])

    def test_inorder_single_node(self) -> None:
        root = Problem.build_from_level([42])
        self.assertEqual(Problem.inorder_of(root), [42])

    def test_preorder_left_skewed(self) -> None:
        root = Problem.build_from_level([1, 2, None, 3])
        self.assertEqual(Problem.preorder_of(root), [1, 2, 3])

    def test_inorder_left_skewed(self) -> None:
        root = Problem.build_from_level([1, 2, None, 3])
        self.assertEqual(Problem.inorder_of(root), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
