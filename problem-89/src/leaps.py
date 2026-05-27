"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expected: int


class Leaps:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, -1, -2, 4, -7, 3], 2, 7),
            TestCase([10, -5, -2, 4, 0, 3], 3, 17),
            TestCase([1, -5], 1, -4),
            TestCase([-4, -3, 4, -2, 0], 2, 0),
            TestCase([1], 1, 1),
            # TestCase("???", "??", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Leaps.get_test_cases():
            actual = solver.max_result(list(tc.nums), tc.k)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
