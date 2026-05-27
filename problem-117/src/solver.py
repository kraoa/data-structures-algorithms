"""You'll implement this."""

from typing import List


class RBTree:
    """
    Time: O(log n) per insert/search, O(n) for inorder. Space: O(n).
    New nodes start red. Fix violations bottom-up: if uncle is red, recolor parent,
    uncle, and grandparent then recurse up. If uncle is black and the path is
    "straight" (LL or RR), do one rotation; if "bent" (LR or RL), double-rotate.
    """

    def insert(self, val: int) -> None:
        pass

    def search(self, val: int) -> bool:
        return False

    def inorder(self) -> List[int]:
        return []
