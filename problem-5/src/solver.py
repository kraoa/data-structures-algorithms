"""You'll implement this."""

from typing import Optional

from tree import TreeNode


class Serializer:
    """
    Converts binary trees to strings and back.

    The encoding format is entirely your choice — the only requirement is that
    deserialize(serialize(tree)) produces a structurally identical tree for
    any valid binary tree, including None (empty tree).
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        return ""

    def deserialize(self, data: str) -> Optional[TreeNode]:
        return None
