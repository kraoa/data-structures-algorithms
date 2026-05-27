"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class TestCase:
    s: str
    expected: str  # one valid longest duplicate; length match suffices


def _check(s: str, actual: str, expected: str) -> bool:
    """Accept any correct-length duplicate substring."""
    if expected == "":
        return actual == ""
    return (
        len(actual) == len(expected)
        and actual in s
        and s.count(actual) >= 2
    )


class Hashing:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("banana", "ana"),
            TestCase("abcd", ""),
            TestCase("aaaa", "aaa"),
            TestCase("aab", "a"),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, str, bool]]:
        results = []
        for tc in Hashing.get_test_cases():
            actual = solver.longest_dup_substring(tc.s)
            passed = _check(tc.s, actual, tc.expected)
            results.append((tc, actual, passed))
        return results
