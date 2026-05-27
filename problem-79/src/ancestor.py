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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Return the first node with the given value via BFS."""
    if root is None:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


@dataclass
class TestCase:
    values: List[Optional[int]]
    p: int
    q: int
    expected: int


class Ancestor:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            TestCase([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            TestCase([1, 2], 1, 2, 1),
            TestCase([3, 1, 2], 1, 2, 3),
            # TestCase("???", "??", "??", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, Optional[int], bool]]:
        results = []
        for tc in Ancestor.get_test_cases():
            root = build_tree(tc.values)
            p_node = find_node(root, tc.p)
            q_node = find_node(root, tc.q)
            result = solver.lowest_common_ancestor(root, p_node, q_node)
            actual = result.val if result is not None else None
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
