"""Read this first."""

from collections import deque
from typing import List, Optional


class TreeNode:
    """A node in a binary tree."""

    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a tree from a level-order list (None = missing node).
    This is the same format LeetCode uses.

    Example: [1, 2, 3, None, None, 4, 5]
        1
       / \\
      2   3
         / \\
        4   5
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
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


def trees_equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    """Returns True if two trees have identical structure and node values."""
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert a tree to its level-order list representation (for display)."""
    if root is None:
        return []
    result: List[Optional[int]] = []
    queue: deque[Optional[TreeNode]] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


class Problem:
    """
    A round-trip serialization test case.

    check(serializer) returns True iff
        deserialize(serialize(tree)) reconstructs the original tree exactly.
    """

    def __init__(self, values: List[Optional[int]]):
        self.values = values
        self.root = from_list(values)

    def check(self, serializer) -> bool:
        """
        serializer must expose:
            serialize(root: TreeNode) -> str
            deserialize(data: str) -> TreeNode
        """
        encoded = serializer.serialize(self.root)
        recovered = serializer.deserialize(encoded)
        return trees_equal(self.root, recovered)

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([1, 2, 3, None, None, 4, 5]),  # LeetCode example
            Problem([]),                             # empty tree
            Problem([1]),                            # single node
            Problem([1, 2]),                         # left child only
            Problem([1, None, 2]),                   # right child only (right-skewed)
            Problem([1, 2, 3, 4, 5, 6, 7]),          # complete tree
            Problem([-10, 9, 20, None, None, 15, 7]), # negative values
            # Problem([...]),                         # add your own edge cases
        ]
