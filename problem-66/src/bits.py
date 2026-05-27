"""Read this first."""

from __future__ import annotations

from collections import Counter
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
            TestCase(nums=[2, 2, 3, 2], expected=3),
            TestCase(nums=[0, 1, 0, 1, 0, 1, 99], expected=99),
            TestCase(nums=[1], expected=1),
            TestCase(nums=[-2, -2, 1, -2], expected=1),
            # TestCase(nums=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.single_number(list(tc.nums))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(nums: List[int]) -> int:
        """Counter-based: find the element whose count mod 3 is 1."""
        counts = Counter(nums)
        for val, cnt in counts.items():
            if cnt % 3 == 1:
                return val
        raise ValueError("No single element found")
