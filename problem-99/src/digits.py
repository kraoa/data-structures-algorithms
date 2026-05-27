"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    n: int
    expected: int


class Digits:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(13, 6),
            TestCase(0, 0),
            TestCase(1, 1),
            TestCase(10, 2),
            TestCase(100, 21),
            TestCase(1000, 301),
            # TestCase(???, ???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Digits.get_test_cases():
            actual = solver.count_digit_one(tc.n)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
