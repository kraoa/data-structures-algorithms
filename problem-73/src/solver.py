"""You'll implement this."""

from typing import List


class Solver:
    """
    Time: O(n * log(sum(nums))), Space: O(1).
    Search the answer in [max(nums), sum(nums)]. For a candidate mid, greedily
    scan left to right counting how many subarrays are needed if no subarray
    may exceed mid; if that count <= k then mid is feasible. Find the smallest
    feasible mid.
    """

    def split_array(self, nums: List[int], k: int) -> int:
        return 0
