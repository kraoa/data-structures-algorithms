"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    p: str
    expected: bool


class Problem:
    """
    Implement regular expression matching supporting two special characters:
      '.'  matches any single character.
      '*'  matches zero or more of the immediately preceding element.

    The match must cover the entire string s (not a substring).

    Example: s="aab", p="c*a*b" → True
      c* matches "" (zero c's), a* matches "aa", b matches "b".
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, bool, bool]]:
        """
        Calls solver.is_match(s, p) for each test case.
        solver must expose .is_match(s: str, p: str) -> bool.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.is_match(tc.s, tc.p)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aa",          "a",        False),  # pattern too short
            TestCase("aa",          "a*",        True),  # a* matches "aa"
            TestCase("ab",          ".*",        True),  # .* matches anything
            TestCase("aab",         "c*a*b",     True),  # c*="" a*="aa" b="b"
            TestCase("mississippi", "mis*is*p*.", False),
            TestCase("",            "a*",        True),  # a* matches empty
            TestCase("",            "",          True),
            TestCase("a",           ".",         True),
            TestCase("aaa",         "a*a",       True),
            TestCase("aaa",         "ab*a",      False),
            # TestCase("???", "???", ?),  # add your own
        ]
