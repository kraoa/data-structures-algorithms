"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    word1: str
    word2: str
    expected: int  # minimum edit distance (insert / delete / replace)


class Problem:
    """
    Given two strings, return the minimum number of single-character operations
    (insert, delete, or replace) needed to transform word1 into word2.

    Example: word1 = "horse", word2 = "ros" → 3
      horse → rorse (replace 'h' with 'r')
      rorse → rose  (delete 'r')
      rose  → ros   (delete 'e')
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.min_distance(word1, word2) for each test case.
        solver must expose .min_distance(word1: str, word2: str) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.min_distance(tc.word1, tc.word2)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("horse",     "ros",       3),   # LeetCode example 1
            TestCase("intention", "execution", 5),   # LeetCode example 2
            TestCase("",          "",          0),
            TestCase("a",         "",          1),
            TestCase("",          "a",         1),
            TestCase("abc",       "abc",       0),
            TestCase("abc",       "axc",       1),   # one replacement
            TestCase("kitten",    "sitting",   3),
            # TestCase("???", "???", ?),  # add your own
        ]
