"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    m: int
    n: int
    k: int
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(m=3, n=3, k=5, expected=3),
            TestCase(m=2, n=3, k=6, expected=6),
            TestCase(m=1, n=1, k=1, expected=1),
            TestCase(m=3, n=3, k=9, expected=9),
            TestCase(m=9, n=9, k=1, expected=1),
            # TestCase(m=???, n=???, k=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.find_kth_number(tc.m, tc.n, tc.k)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
