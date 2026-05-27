"""Driver tests — all must pass out of the box."""

import unittest
from typing import Optional
from tree import Problem, TestCase, TreeNode, from_list


class TestTree(unittest.TestCase):

    @staticmethod
    def _max_path_sum(root: Optional[TreeNode]) -> int:
        """Reference DFS: track best path through each node."""
        best = [float("-inf")]

        def gain(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best[0] = max(best[0], node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return int(best[0])

    def test_expected_values_match_reference(self) -> None:
        for tc in Problem.get_test_cases():
            root = from_list(tc.values)
            self.assertEqual(tc.expected, self._max_path_sum(root))

    def test_from_list_builds_correct_structure(self) -> None:
        root = from_list([1, 2, 3])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

    def test_from_list_handles_none_gaps(self) -> None:
        root = from_list([-10, 9, 20, None, None, 15, 7])
        self.assertIsNone(root.left.left)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"max_path_sum": lambda self, r: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
