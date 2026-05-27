"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    text1: str
    text2: str
    expected: int


class Problem:
    """
    Given two strings, return the length of their longest common subsequence.
    A subsequence is formed by deleting some (or no) characters without
    changing the relative order of the remaining characters.

    Example: text1 = "abcde", text2 = "ace" → 3  ("ace")
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.lcs(text1, text2) for each test case.
        solver must expose .lcs(text1: str, text2: str) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.lcs(tc.text1, tc.text2)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("abcde", "ace",           3),  # LeetCode example 1
            TestCase("abc",   "abc",            3),  # LeetCode example 2: identical
            TestCase("abc",   "def",            0),  # no common characters
            TestCase("",      "abc",            0),  # empty string
            TestCase("a",     "a",              1),  # single character match
            TestCase("oxcpqrsvwf", "shmtulqrypy", 2),
            TestCase("bsbininm", "jmjkbkjkv",   1),
            # TestCase("???", "??", ??),  # add your own
        ]
