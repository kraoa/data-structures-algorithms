"""Tests for Problem. Verifies build, preorder, and stored expected values."""

import unittest
from tree import Problem


class ProblemTest(unittest.TestCase):

    def test_preorder_matches_expected(self) -> None:
        """The stored expected values equal the preorder of each built tree."""
        for tc in Problem.get_test_cases():
            if not tc.vals:
                self.assertEqual(tc.expected, [])
                continue
            root = Problem.build(tc.vals)
            self.assertEqual(Problem.preorder(root), tc.expected,
                             f"vals={tc.vals}: preorder mismatch")

    def test_build_empty(self) -> None:
        self.assertIsNone(Problem.build([]))

    def test_build_single(self) -> None:
        root = Problem.build([1])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_right_chain_single(self) -> None:
        root = Problem.build([5])
        self.assertEqual(Problem.right_chain(root), [5])

    def test_right_chain_follows_right_only(self) -> None:
        root = Problem.build([1, 2, 3])
        # right_chain only follows right pointers, not left.
        self.assertEqual(Problem.right_chain(root), [1, 3])


if __name__ == "__main__":
    unittest.main()
