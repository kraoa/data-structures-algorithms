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
    preorder: List[int]
    inorder: List[int]
    level_order: List[Optional[int]]  # level-order representation for reference


class Problem:
    """
    Given the preorder and inorder traversals of a binary tree (all values are
    unique), reconstruct and return the root of the tree.

    Example: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
             → tree: 3 (left=9, right=20 (left=15, right=7))
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def build_from_level(vals: List[Optional[int]]) -> Optional[TreeNode]:
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
    def preorder_of(root: Optional[TreeNode]) -> List[int]:
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
    def inorder_of(root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[Optional[TreeNode]] = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

    def run(self, solver) -> List[Tuple[TestCase, bool]]:
        """
        Calls solver.build_tree(preorder, inorder) for each test case.
        solver must expose .build_tree(preorder: List[int], inorder: List[int])
                           -> Optional[TreeNode].
        Validates by re-extracting traversals from the returned tree.
        Returns (test_case, passed).
        """
        results = []
        for tc in self.test_cases:
            root = solver.build_tree(list(tc.preorder), list(tc.inorder))
            actual_pre = Problem.preorder_of(root)
            actual_in = Problem.inorder_of(root)
            passed = actual_pre == tc.preorder and actual_in == tc.inorder
            results.append((tc, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],
                     [3, 9, 20, None, None, 15, 7]),            # LeetCode example 1
            TestCase([-1], [-1], [-1]),                          # LeetCode example 2
            TestCase([1, 2], [2, 1], [1, 2]),                    # left-skewed
            TestCase([1, 2], [1, 2], [1, None, 2]),              # right-skewed
            TestCase([4, 2, 1, 3, 6, 5, 7],
                     [1, 2, 3, 4, 5, 6, 7],
                     [4, 2, 6, 1, 3, 5, 7]),                    # balanced BST
            # TestCase([???], [???], [???]),  # add your own
        ]
