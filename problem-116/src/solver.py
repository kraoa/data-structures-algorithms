"""You'll implement this."""

from typing import List, Optional


class AVLTree:
    """
    Time: O(log n) per insert/search, O(n) for inorder. Space: O(n).
    Each node stores a height; balance factor = height(left) - height(right).
    After inserting into a subtree, update heights on the way back up. If
    |balance| > 1, apply LL (right rotate), RR (left rotate), LR (left then
    right rotate), or RL (right then left rotate) to restore balance.
    """

    def insert(self, val: int) -> None:
        pass

    def search(self, val: int) -> bool:
        return False

    def inorder(self) -> List[int]:
        return []
