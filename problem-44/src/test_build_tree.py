"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from reconstruction import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     root = solver.build_tree([3,9,20,15,7], [9,3,15,20,7])
    #     from reconstruction import Problem as P
    #     self.assertEqual(P.preorder_of(root), [3,9,20,15,7])
    #     self.assertEqual(P.inorder_of(root), [9,3,15,20,7])

    # def test_single_node(self) -> None:
    #     solver = Solver()
    #     root = solver.build_tree([-1], [-1])
    #     self.assertEqual(root.val, -1)
    #     self.assertIsNone(root.left)
    #     self.assertIsNone(root.right)

    # def test_left_skewed(self) -> None:
    #     solver = Solver()
    #     root = solver.build_tree([1,2], [2,1])
    #     self.assertEqual(root.val, 1)
    #     self.assertEqual(root.left.val, 2)
    #     self.assertIsNone(root.right)

    # def test_index_map_avoids_wrong_root(self) -> None:
    #     # Without the inorder index map, duplicate-value confusion can pick the wrong root.
    #     solver = Solver()
    #     root = solver.build_tree([4,2,1,3,6,5,7], [1,2,3,4,5,6,7])
    #     from reconstruction import Problem as P
    #     self.assertEqual(P.inorder_of(root), [1,2,3,4,5,6,7])


if __name__ == "__main__":
    unittest.main()
