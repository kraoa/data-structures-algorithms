"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    digits: List[str]
    n: int
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(digits=["1", "3", "5", "7"], n=100, expected=20),
            TestCase(digits=["1", "4", "9"], n=8, expected=2),
            TestCase(digits=["7"], n=8, expected=1),
            TestCase(digits=["1", "2"], n=25, expected=6),
            # TestCase(digits=["???"], n=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.at_most_n_given_digit_set(list(tc.digits), tc.n)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
