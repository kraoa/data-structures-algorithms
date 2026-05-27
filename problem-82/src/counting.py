"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    t: str
    expected: int


class Counting:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("rabbbit", "rabbit", 3),
            TestCase("babgbag", "bag", 5),
            TestCase("a", "a", 1),
            TestCase("a", "b", 0),
            TestCase("aa", "a", 2),
            TestCase("", "", 1),
            # TestCase("???", "??", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Counting.get_test_cases():
            actual = solver.num_distinct(tc.s, tc.t)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
