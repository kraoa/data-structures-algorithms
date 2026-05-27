"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    nums: List[int]
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(nums=[3, 10, 5, 25, 2, 8], expected=28),
            TestCase(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], expected=127),
            TestCase(nums=[0], expected=0),
            TestCase(nums=[4, 6], expected=2),
            # TestCase(nums=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.find_maximum_xor(list(tc.nums))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(nums: List[int]) -> int:
        """O(n^2): check all pairs and track the maximum XOR."""
        n = len(nums)
        best = 0
        for i in range(n):
            for j in range(i, n):
                best = max(best, nums[i] ^ nums[j])
        return best
