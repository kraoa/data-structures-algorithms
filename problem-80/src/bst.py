"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from BFS-order list; None means missing node."""
    if not values or values[0] is None:
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
    expected: bool


class BST:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 1, 3], True),
            TestCase([5, 1, 4, None, None, 3, 6], False),
            TestCase([2, 2, 2], False),
            TestCase([1], True),
            TestCase([5, 4, 6, None, None, 3, 7], False),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, bool, bool]]:
        results = []
        for tc in BST.get_test_cases():
            root = build_tree(tc.values)
            actual = solver.is_valid_bst(root)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
