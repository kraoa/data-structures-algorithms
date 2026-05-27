"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    lower: int
    upper: int
    expected: int


class RangeCount:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([-2, 5, -1], -2, 2, 3),
            TestCase([0], 0, 0, 1),
            TestCase([1, 2, 3], 0, 3, 4),
            TestCase([-1], -1, 0, 1),
            # TestCase("???", ??, ??, ??),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in RangeCount.get_test_cases():
            actual = solver.count_range_sum(list(tc.nums), tc.lower, tc.upper)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
