"""Tests for RBTree solver. Assertions are commented out until implemented."""

import unittest
from rb_tree import Problem, Op
from solver import RBTree


class TestRBTreeSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(RBTree)

    # def test_inorder_sorted(self) -> None:
    #     tree = RBTree()
    #     for v in [10, 20, 30, 15, 25]:
    #         tree.insert(v)
    #     self.assertEqual(tree.inorder(), [10, 15, 20, 25, 30])

    # def test_search(self) -> None:
    #     tree = RBTree()
    #     tree.insert(7)
    #     tree.insert(3)
    #     self.assertTrue(tree.search(7))
    #     self.assertFalse(tree.search(99))

    # def test_complex_insertions(self) -> None:
    #     # A sequence that triggers recoloring and both rotation types.
    #     tree = RBTree()
    #     for v in [7, 3, 18, 10, 22, 8, 26]:
    #         tree.insert(v)
    #     self.assertEqual(tree.inorder(), [3, 7, 8, 10, 18, 22, 26])


if __name__ == "__main__":
    unittest.main()
