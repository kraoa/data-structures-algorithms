"""Read this first."""

from dataclasses import dataclass, field
from typing import List, Set, Tuple


@dataclass
class TestCase:
    s: str
    word_dict: Set[str]
    expected: List[str]  # all valid sentences; order does not matter


class Problem:
    """
    Given string s and a dictionary of words, return all ways to segment s into
    a space-separated sequence of dictionary words.

    Example:
        s = "catsanddog"
        wordDict = {"cat", "cats", "and", "sand", "dog"}
        result   = ["cats and dog", "cat sand dog"]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[str], bool]]:
        """
        Calls solver.word_break(s, word_dict) for each test case.
        solver must expose .word_break(s: str, word_dict: Set[str]) -> List[str].
        Returns (test_case, actual_result, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.word_break(tc.s, tc.word_dict)
            passed = self._check(tc.s, tc.word_dict, actual, tc.expected)
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _check(s: str, word_dict: Set[str], result: List[str], expected: List[str]) -> bool:
        """
        Returns True iff result is exactly the set of valid segmentations (order-insensitive).
        Each sentence in result must:
          - consist entirely of words from word_dict,
          - concatenate (without spaces) to s.
        """
        for sentence in result:
            words = sentence.split()
            if "".join(words) != s:
                return False
            if not all(w in word_dict for w in words):
                return False
        result_set = {tuple(sentence.split()) for sentence in result}
        expected_set = {tuple(sentence.split()) for sentence in expected}
        return result_set == expected_set

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                "catsanddog",
                {"cat", "cats", "and", "sand", "dog"},
                ["cats and dog", "cat sand dog"],
            ),
            TestCase(
                "pineapplepenapple",
                {"apple", "pen", "applepen", "pine", "pineapple"},
                ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
            ),
            TestCase(
                "abcdef",
                {"abc", "abd", "ef", "gh"},
                [],  # no valid segmentation
            ),
            TestCase("a", {"a"}, ["a"]),
            # TestCase("???", {...}, [...]),  # add your own
        ]
