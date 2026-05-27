"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: str


class Problem:
    """
    Decode a string encoded as k[pattern], where the pattern inside brackets is
    repeated exactly k times. Patterns can be nested.

    Examples:
        "3[a]2[bc]"   → "aaabcbc"
        "3[a2[c]]"    → "accaccacc"
        "2[abc]3[cd]ef" → "abcabccdcdcdef"
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, str, bool]]:
        """
        Calls solver.decode_string(s) for each test case.
        solver must expose .decode_string(s: str) -> str.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.decode_string(tc.s)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("3[a]2[bc]",        "aaabcbc"),          # LeetCode example 1
            TestCase("3[a2[c]]",          "accaccacc"),        # LeetCode example 2: nested
            TestCase("2[abc]3[cd]ef",     "abcabccdcdcdef"),   # LeetCode example 3
            TestCase("abc",               "abc"),               # no encoding
            TestCase("10[a]",             "a" * 10),            # multi-digit count
            TestCase("1[b]",              "b"),                  # k=1
            TestCase("2[3[a]]",           "aaaaaa"),            # double nesting
            # TestCase("???", "???"),  # add your own
        ]
