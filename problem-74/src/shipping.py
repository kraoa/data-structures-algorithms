"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    weights: List[int]
    days: int
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5, expected=15),
            TestCase(weights=[3, 2, 2, 4, 1, 4], days=3, expected=6),
            TestCase(weights=[1, 2, 3, 1, 1], days=4, expected=3),
            TestCase(weights=[10], days=1, expected=10),
            # TestCase(weights=???, days=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.ship_within_days(list(tc.weights), tc.days)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _feasible(weights: List[int], days: int, cap: int) -> bool:
        """Greedy packing: count how many days are needed at this capacity."""
        current = 0
        needed = 1
        for w in weights:
            if current + w > cap:
                needed += 1
                current = 0
            current += w
        return needed <= days

    @staticmethod
    def brute_force(weights: List[int], days: int) -> int:
        """Linear scan from max(weights) upward until feasible."""
        cap = max(weights)
        while not Problem._feasible(weights, days, cap):
            cap += 1
        return cap
