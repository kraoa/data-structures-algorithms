"""Tests for Problem helpers. All of this is just boilerplate to make test cases compact and understandable."""

import unittest
from typing import Optional

from tree import TreeNode, Problem, from_list, to_list, trees_equal


class ProblemTest(unittest.TestCase):

    def test_from_list_to_list_roundtrip(self) -> None:
        """Building a tree from a list and converting back should be lossless."""
        cases = [
            [1, 2, 3, None, None, 4, 5],
            [],
            [1],
            [1, 2],
            [1, None, 2],
            [1, 2, 3, 4, 5, 6, 7],
            [-10, 9, 20, None, None, 15, 7],
        ]
        for values in cases:
            root = from_list(values)
            self.assertEqual(to_list(root), values, f"round-trip failed for {values}")

    def test_trees_equal_same_structure(self) -> None:
        a = from_list([1, 2, 3])
        b = from_list([1, 2, 3])
        self.assertTrue(trees_equal(a, b))

    def test_trees_equal_different_structure(self) -> None:
        left_child  = from_list([1, 2])        # 2 is a left child
        right_child = from_list([1, None, 2])  # 2 is a right child
        self.assertFalse(trees_equal(left_child, right_child))

    def test_trees_equal_different_value(self) -> None:
        a = from_list([1, 2, 3])
        b = from_list([1, 2, 99])
        self.assertFalse(trees_equal(a, b))

    def test_trees_equal_both_none(self) -> None:
        self.assertTrue(trees_equal(None, None))

    def test_problem_check_correct(self) -> None:
        """check() returns True when deserialize reconstructs the tree correctly."""

        class PassthroughSerializer:
            def serialize(self, root: Optional[TreeNode]) -> str:
                self._root = root
                return "token"

            def deserialize(self, data: str) -> Optional[TreeNode]:
                return self._root

        problem = Problem([1, 2, 3, None, None, 4, 5])
        self.assertTrue(problem.check(PassthroughSerializer()))

    def test_problem_check_wrong(self) -> None:
        """check() returns False when the deserialized tree differs."""

        class CorruptSerializer:
            def serialize(self, root: Optional[TreeNode]) -> str:
                return "token"

            def deserialize(self, data: str) -> Optional[TreeNode]:
                return TreeNode(999)

        problem = Problem([1, 2, 3])
        self.assertFalse(problem.check(CorruptSerializer()))


if __name__ == "__main__":
    unittest.main()
