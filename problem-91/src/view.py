"""Read this first."""

from collections import deque
from dataclasses import dataclass
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


@dataclass
class TestCase:
    values: List[Optional[int]]
    expected: List[int]


class Problem:
    """
    Given the root of a binary tree, return the values of the nodes you can see
    from the right side, ordered from top to bottom.

    Example: values = [1,2,3,null,5,null,4] -> [1, 3, 4]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in self.test_cases:
            root = build_tree(tc.values)
            actual = solver.right_side_view(root)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 2, 3, None, 5, None, 4], [1, 3, 4]),  # LeetCode example 1
            TestCase([1, None, 3],                 [1, 3]),     # LeetCode example 2
            TestCase([],                           []),          # empty tree
            TestCase([1],                          [1]),         # single node
            TestCase([1, 2, 3, 4],                 [1, 3, 4]),  # left-heavy subtree visible
            # TestCase([...], [...]),  # add your own
        ]
