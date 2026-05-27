"""Read this first."""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


def from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from level-order values (None = missing node)."""
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
    values: List[Optional[int]]  # level-order; None = missing node
    expected: int                # maximum path sum


class Problem:
    """
    A path in a binary tree is a sequence of nodes where each pair of
    adjacent nodes has an edge. The path must contain at least one node
    and does not need to pass through the root. Return the maximum sum of
    any such path.

    Example: [-10,9,20,None,None,15,7] → 42  (15+20+7)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            root = from_list(list(tc.values))
            actual = solver.max_path_sum(root)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 2, 3], 6),                              # 2+1+3
            TestCase([-10, 9, 20, None, None, 15, 7], 42),       # 15+20+7
            TestCase([1], 1),                                    # single node
            TestCase([-3], -3),                                  # negative-only tree
            TestCase([2, -1, None], 2),                          # skip negative child
            TestCase([-1, -2, 3], 3),                            # best is single node
            # TestCase([...], ?),                                # add your own
        ]
