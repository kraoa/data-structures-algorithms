"""You'll implement this."""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solver:
    def flatten(self, root: Optional[TreeNode]) -> None:
        return
