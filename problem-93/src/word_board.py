"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    board: List[List[str]]
    words: List[str]
    expected: List[str]  # sorted


class WordBoard:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
                words=["oath","pea","eat","rain"],
                expected=["eat","oath"],
            ),
            TestCase(
                board=[["a","b"],["c","d"]],
                words=["abdc","abcd"],
                expected=["abdc"],
            ),
            TestCase(
                board=[["a"]],
                words=["a"],
                expected=["a"],
            ),
            TestCase(
                board=[["a","a"]],
                words=["aaa"],
                expected=[],
            ),
            # TestCase(board=???, words=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[str], bool]]:
        results = []
        for tc in WordBoard.get_test_cases():
            actual = solver.find_words(copy.deepcopy(tc.board), list(tc.words))
            actual_sorted = sorted(actual)
            passed = actual_sorted == sorted(tc.expected)
            results.append((tc, actual_sorted, passed))
        return results
