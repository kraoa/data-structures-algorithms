"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    words: List[str]
    expected: List[List[int]]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                words=["abcd", "dcba", "lls", "s", "sssll"],
                expected=[[0, 1], [1, 0], [2, 4], [3, 2]],
            ),
            TestCase(
                words=["bat", "tab", "cat"],
                expected=[[0, 1], [1, 0]],
            ),
            TestCase(
                words=["a", ""],
                expected=[[0, 1], [1, 0]],
            ),
            # TestCase(words=["???", "??"], expected=[]),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.palindrome_pairs(list(tc.words))
            passed = sorted(actual) == sorted(tc.expected)
            results.append((tc, actual, passed))
        return results
