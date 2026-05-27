"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s1: str
    s2: str
    s3: str
    expected: bool


class Problem:
    """
    Given strings s1, s2, and s3, determine if s3 is formed by interleaving s1
    and s2. An interleaving preserves the relative order of characters from each
    source string.

    Example: s1="aabcc", s2="dbbca", s3="aadbbcbcac" -> True
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, bool, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.is_interleave(tc.s1, tc.s2, tc.s3)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("aabcc", "dbbca", "aadbbcbcac",  True),   # LeetCode example 1
            TestCase("aabcc", "dbbca", "aadbbbaccc",  False),  # LeetCode example 2
            TestCase("",      "",      "",             True),   # both empty
            TestCase("a",     "b",     "ab",           True),
            TestCase("a",     "b",     "ba",           True),
            TestCase("ab",    "cd",    "acbd",         True),
            TestCase("ab",    "cd",    "abdc",         False),  # violates s2 order (d before c)
            TestCase("aab",   "abc",   "aaabbc",       True),
            # TestCase("???", "???", "???", ???),  # add your own
        ]
