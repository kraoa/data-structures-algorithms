"""Read this first."""

from collections import deque
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: int  # minimum jumps to reach last index (guaranteed reachable)


class Problem:
    """
    You are at index 0. nums[i] is the maximum jump length at position i.
    Return the minimum number of jumps to reach the last index.
    It is guaranteed the last index is always reachable.

    Example: [2,3,1,1,4] → 2  (0 → 1 → 4)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.min_jumps(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 3, 1, 1, 4], 2),   # LeetCode example 1
            TestCase([2, 3, 0, 1, 4], 2),   # LeetCode example 2
            TestCase([1], 0),               # single element, already at end
            TestCase([1, 1, 1, 1], 3),      # forced one-step hops
            TestCase([5, 1, 1, 1, 1], 1),   # one big jump covers all
            TestCase([1, 2, 3, 4, 5], 3),   # 0→1→3→4
            # TestCase([...], ?),           # add your own
        ]
