"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: int


class Printer:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aaabbb", 2),
            TestCase("aba", 2),
            TestCase("a", 1),
            TestCase("aa", 1),
            TestCase("leetcode", 6),
            # TestCase("???", ??),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Printer.get_test_cases():
            actual = solver.strange_printer(tc.s)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
