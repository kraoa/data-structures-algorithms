"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: List[int]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("banana", [5, 3, 1, 0, 4, 2]),
            TestCase("a", [0]),
            TestCase("ab", [0, 1]),
            TestCase("aab", [0, 1, 2]),
            TestCase("mississippi", [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]),
            # TestCase("???", [???]),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.build(tc.s)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
