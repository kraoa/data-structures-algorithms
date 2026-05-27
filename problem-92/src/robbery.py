"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """BFS-list builder: values[0] is root; None means no node."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
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
    expected: int


class Robbery:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([3, 2, 3, None, 3, None, 1], 7),
            TestCase([3, 4, 5, 1, 3, None, 1], 9),
            TestCase([1], 1),
            TestCase([1, 2], 2),
            TestCase([4, 1, None, 2, None, 3], 7),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Robbery.get_test_cases():
            root = build_tree(list(tc.values))
            actual = solver.rob(root)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
