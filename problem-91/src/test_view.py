"""Tests for the View driver."""

import unittest
from collections import deque
from typing import List, Optional

from view import Problem, TreeNode, build_tree


class TestViewDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(root: Optional[TreeNode]) -> List[int]:
        """BFS level-order; collect the last node value at each level."""
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            root = build_tree(tc.values)
            bf = self._brute_force(root)
            self.assertEqual(tc.expected, bf, f"values={tc.values!r}")


if __name__ == "__main__":
    unittest.main()
