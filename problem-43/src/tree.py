"""Read this first."""

from collections import deque
from dataclasses import dataclass
from typing import Deque, List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


@dataclass
class TestCase:
    vals: List[Optional[int]]  # level-order input (None = absent node)
    expected: List[int]         # preorder traversal of the original tree


class Problem:
    """
    Flatten a binary tree in-place so that every node's left child is None and
    the right children form the pre-order traversal of the original tree.

    Example: tree built from [1,2,5,3,4,None,6]
             → right-chain: 1 → 2 → 3 → 4 → 5 → 6
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def build(vals: List[Optional[int]]) -> Optional[TreeNode]:
        """Build a tree from level-order values; None entries are absent nodes."""
        if not vals:
            return None
        root = TreeNode(vals[0])
        queue: Deque[TreeNode] = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root

    @staticmethod
    def preorder(root: Optional[TreeNode]) -> List[int]:
        """Return preorder traversal values."""
        result: List[int] = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    @staticmethod
    def right_chain(root: Optional[TreeNode]) -> List[int]:
        """Follow right pointers from root; return all values in order."""
        result: List[int] = []
        node = root
        while node:
            result.append(node.val)
            node = node.right
        return result

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        """
        Calls solver.flatten(root) for each test case.
        solver must expose .flatten(root: Optional[TreeNode]) -> None
        (modifies the tree in-place).
        Returns (test_case, actual_right_chain, passed).
        """
        results = []
        for tc in self.test_cases:
            root = Problem.build(tc.vals)
            solver.flatten(root)
            actual = Problem.right_chain(root)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),  # LeetCode example
            TestCase([],                        []),                    # empty tree
            TestCase([0],                       [0]),                   # single node
            TestCase([1, 2, None],              [1, 2]),                # left only
            TestCase([1, None, 2],              [1, 2]),                # right only
            # TestCase([???], [???]),  # add your own
        ]
