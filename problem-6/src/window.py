"""Read this first."""

from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    t: str
    expected: str  # "" means no valid window exists


class Problem:
    """
    Find the minimum-length contiguous substring of s that contains every
    character in t (with correct multiplicity). Return "" if none exists.

    Example: s = "ADOBECODEBANC", t = "ABC" → "BANC"
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, str, bool]]:
        """
        Calls solver.min_window(s, t) for each test case.
        solver must expose .min_window(s: str, t: str) -> str.
        Returns (test_case, actual_result, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.min_window(tc.s, tc.t)
            passed = self._check(tc.s, tc.t, actual, tc.expected)
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _check(s: str, t: str, result: str, expected: str) -> bool:
        """
        Returns True iff result is a correct minimum-window answer:
          - When expected is "": result must also be "".
          - Otherwise: result must be a substring of s, contain all characters
            of t with sufficient multiplicity, and match the optimal length.
            (Multiple valid windows of equal length are all accepted.)
        """
        if expected == "":
            return result == ""
        if result == "":
            return False
        if result not in s:
            return False
        need = Counter(t)
        have = Counter(result)
        if any(have[ch] < n for ch, n in need.items()):
            return False
        return len(result) == len(expected)

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("ADOBECODEBANC",       "ABC",  "BANC"),
            TestCase("a",                   "a",    "a"),
            TestCase("a",                   "aa",   ""),     # not enough a's in s
            TestCase("aa",                  "aa",   "aa"),
            TestCase("ab",                  "b",    "b"),
            TestCase("cabwefgewcwaefgcf",   "cae",  "cwae"),
            # TestCase("???", "??", "??"),                   # add your own
        ]
