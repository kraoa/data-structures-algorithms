"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from robbery import Robbery, build_tree
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        root = build_tree([3, 2, 3, None, 3, None, 1])
        solver.rob(root)  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     root = build_tree([3, 2, 3, None, 3, None, 1])
    #     self.assertEqual(solver.rob(root), 7)

    # def test_second_example(self) -> None:
    #     solver = Solver()
    #     root = build_tree([3, 4, 5, 1, 3, None, 1])
    #     self.assertEqual(solver.rob(root), 9)

    # def test_single_node(self) -> None:
    #     solver = Solver()
    #     root = build_tree([1])
    #     self.assertEqual(solver.rob(root), 1)

    # def test_chain_grandchild(self) -> None:
    #     # Rob root(4) and great-grandchild(3) = 7; greedy fails here.
    #     solver = Solver()
    #     root = build_tree([4, 1, None, 2, None, 3])
    #     self.assertEqual(solver.rob(root), 7)


if __name__ == "__main__":
    unittest.main()
