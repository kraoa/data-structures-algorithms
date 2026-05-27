"""You'll implement this."""

from typing import Optional


class IntervalTree:
    """
    Time: O(log n + k) per query where k = output size, O(log n) amortized insert. Space: O(n).
    Each node stores an interval [lo, hi] and the maximum hi in its subtree.
    Insert like a BST on lo, updating max_hi on the way up. During query(point),
    descend into the left subtree only if its max_hi >= point (pruning), then
    always check the current node, then descend right similarly.
    """

    def insert(self, lo: int, hi: int) -> None:
        pass

    def query(self, point: int) -> int:
        return 0
