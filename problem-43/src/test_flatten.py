"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from tree import Problem, TreeNode
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     root = Problem.build([1, 2, 5, 3, 4, None, 6])
    #     solver.flatten(root)
    #     self.assertEqual(Problem.right_chain(root), [1, 2, 3, 4, 5, 6])

    # def test_no_left_children_after_flatten(self) -> None:
    #     solver = Solver()
    #     root = Problem.build([1, 2, 5, 3, 4, None, 6])
    #     solver.flatten(root)
    #     node = root
    #     while node:
    #         self.assertIsNone(node.left)
    #         node = node.right

    # def test_empty_tree(self) -> None:
    #     solver = Solver()
    #     solver.flatten(None)   # should not raise

    # def test_single_node(self) -> None:
    #     solver = Solver()
    #     root = Problem.build([0])
    #     solver.flatten(root)
    #     self.assertEqual(Problem.right_chain(root), [0])


if __name__ == "__main__":
    unittest.main()
