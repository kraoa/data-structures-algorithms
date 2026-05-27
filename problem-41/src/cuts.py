"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: List[List[str]]   # all partitions where every part is a palindrome


class Problem:
    """
    Partition string s so that every substring in the partition is a palindrome.
    Return all possible such partitions.

    Example: s = "aab"
             → [["a","a","b"], ["aa","b"]]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def _normalize(partitions: List[List[str]]) -> List[Tuple[str, ...]]:
        return sorted(tuple(p) for p in partitions)

    def run(self, solver) -> List[Tuple[TestCase, List[List[str]], bool]]:
        """
        Calls solver.partition(s) for each test case.
        solver must expose .partition(s: str) -> List[List[str]].
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.partition(tc.s)
            passed = Problem._normalize(actual) == Problem._normalize(tc.expected)
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aab", [["a","a","b"], ["aa","b"]]),              # LeetCode example 1
            TestCase("a",   [["a"]]),                                   # LeetCode example 2
            TestCase("aba", [["a","b","a"], ["aba"]]),
            TestCase("aa",  [["a","a"], ["aa"]]),
            # TestCase("???", [???]),  # add your own
        ]
