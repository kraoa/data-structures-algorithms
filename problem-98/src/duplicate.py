"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: int


class Duplicate:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 3, 4, 2, 2], 2),
            TestCase([3, 1, 3, 4, 2], 3),
            TestCase([1, 1], 1),
            TestCase([1, 1, 2], 1),
            TestCase([2, 2, 2, 2, 2], 2),
            # TestCase("???", ??),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Duplicate.get_test_cases():
            # Pass a copy; solver must not modify the array.
            actual = solver.find_duplicate(list(tc.nums))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
