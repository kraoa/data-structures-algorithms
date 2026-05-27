"""Tests for AVLTree solver. Assertions are commented out until implemented."""

import unittest
from avl_tree import Problem, Op
from solver import AVLTree


class TestAVLTreeSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(AVLTree)

    # def test_inorder_sorted(self) -> None:
    #     problem = Problem([
    #         Op("insert", 10, None), Op("insert", 20, None), Op("insert", 30, None),
    #         Op("inorder", None, [10, 20, 30]),
    #     ])
    #     results = problem.run(AVLTree)
    #     _, actual, passed = results[-1]
    #     self.assertTrue(passed, f"inorder expected [10,20,30], got {actual}")

    # def test_search(self) -> None:
    #     tree = AVLTree()
    #     tree.insert(5)
    #     tree.insert(3)
    #     self.assertTrue(tree.search(5))
    #     self.assertFalse(tree.search(99))

    # def test_left_rotation_balance(self) -> None:
    #     # Inserting 10, 20, 30 forces an LL rotation; tree must still be balanced.
    #     tree = AVLTree()
    #     for v in [10, 20, 30]:
    #         tree.insert(v)
    #     self.assertEqual(tree.inorder(), [10, 20, 30])


if __name__ == "__main__":
    unittest.main()
