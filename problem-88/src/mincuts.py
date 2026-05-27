"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: int


class MinCuts:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aab", 1),
            TestCase("a", 0),
            TestCase("ab", 1),
            TestCase("aaaa", 0),
            TestCase("leet", 2),
            TestCase("abcba", 0),
            TestCase("abacaba", 0),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in MinCuts.get_test_cases():
            actual = solver.min_cut(tc.s)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
