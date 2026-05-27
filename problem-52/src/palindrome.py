"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: str  # one valid answer; any palindromic substring of the same length is accepted


class Problem:
    """
    Given a string s, return the longest palindromic substring.
    If multiple palindromes tie for the maximum length, any is accepted.

    Example: s = "babad" -> "bab" (or "aba")
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, str, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.longest_palindrome(tc.s)
            passed = self._check(tc.s, actual, tc.expected)
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _check(s: str, result: str, expected: str) -> bool:
        """Any palindromic substring of s matching the optimal length is accepted."""
        if len(result) != len(expected):
            return False
        if result and result not in s:
            return False
        return result == result[::-1]

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("babad",   "bab"),      # LeetCode example 1; "aba" also valid
            TestCase("cbbd",    "bb"),        # LeetCode example 2
            TestCase("a",       "a"),         # single character
            TestCase("ac",      "a"),         # no palindrome longer than 1; "c" also valid
            TestCase("racecar", "racecar"),   # whole string is a palindrome
            TestCase("abcba",   "abcba"),     # odd-length full palindrome
            TestCase("bb",      "bb"),        # even-length palindrome
            TestCase("",        ""),          # empty string
            # TestCase("???", "??"),  # add your own
        ]
