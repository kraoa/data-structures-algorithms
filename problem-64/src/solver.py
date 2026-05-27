"""You'll implement this."""

from __future__ import annotations

from typing import List


class NumArray:
    """
    Target: O(log n) per update and sum_range, O(n) space.
    Store a BIT array of length n+1; update propagates changes up via i += i & -i;
    prefix-sum query accumulates down via i -= i & -i. sum_range(i,j) = query(j+1) - query(i).
    """

    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)

    def update(self, i: int, val: int) -> None:
        return None

    def sum_range(self, i: int, j: int) -> int:
        return 0
