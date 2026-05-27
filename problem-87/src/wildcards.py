"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    p: str
    expected: bool


class Wildcards:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aa", "a", False),
            TestCase("aa", "*", True),
            TestCase("cb", "?a", False),
            TestCase("adceb", "*a*b", True),
            TestCase("acdcb", "a*c?b", False),
            TestCase("", "*", True),
            TestCase("", "", True),
            # TestCase("???", "??", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, bool, bool]]:
        results = []
        for tc in Wildcards.get_test_cases():
            actual = solver.is_match(tc.s, tc.p)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
