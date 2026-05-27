"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    text: str
    pattern: str
    expected: List[int]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(text="aabcaabxaaaz", pattern="aab", expected=[0, 4]),
            TestCase(text="abababab", pattern="abab", expected=[0, 2, 4]),
            TestCase(text="aaaa", pattern="aa", expected=[0, 1, 2]),
            TestCase(text="hello world", pattern="world", expected=[6]),
            TestCase(text="abc", pattern="xyz", expected=[]),
            TestCase(text="abcabc", pattern="abc", expected=[0, 3]),
            # TestCase(text="???", pattern="???", expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.find_all(tc.text, tc.pattern)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(text: str, pattern: str) -> List[int]:
        """O(n*m) naive: try matching at every starting position."""
        n, m = len(text), len(pattern)
        if m == 0:
            return list(range(n + 1))
        result = []
        for i in range(n - m + 1):
            if text[i: i + m] == pattern:
                result.append(i)
        return result
