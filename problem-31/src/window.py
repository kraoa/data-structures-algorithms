"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    p: str
    expected: List[int]  # sorted starting indices of p's anagrams in s


class Problem:
    """
    Given strings s and p, return all starting indices in s where a
    substring is an anagram of p. An anagram uses exactly the same
    characters with the same frequencies.

    Example: s="cbaebabacd", p="abc" → [0, 6]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in self.test_cases:
            actual = sorted(solver.find_anagrams(tc.s, tc.p))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("cbaebabacd", "abc", [0, 6]),
            TestCase("abab", "ab", [0, 1, 2]),
            TestCase("aa", "bb", []),
            TestCase("a", "a", [0]),
            TestCase("baa", "aa", [1]),
            # TestCase("???", "???", [...]),  # add your own
        ]
