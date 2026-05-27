"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    board: List[List[str]]
    word: str
    expected: bool


class Problem:
    """
    Given an m×n character grid and a word, return True if the word can be
    constructed by following a path of adjacent (horizontally or vertically)
    cells. Each cell may be used at most once per path.

    Example:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCCED"  → True
        word = "SEE"     → True
        word = "ABCB"    → False  (can't reuse B)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, bool, bool]]:
        """
        Calls solver.exist(board, word) for each test case.
        solver must expose .exist(board: List[List[str]], word: str) -> bool.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.exist(copy.deepcopy(tc.board), tc.word)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        return [
            TestCase(board, "ABCCED", True),   # LeetCode example 1
            TestCase(board, "SEE",    True),   # LeetCode example 2
            TestCase(board, "ABCB",  False),   # LeetCode example 3: revisit required
            TestCase([["a"]],        "a", True),   # single cell match
            TestCase([["a","b"],
                      ["c","d"]],    "abdc", True),  # wraps around
            TestCase([["a","b"],
                      ["c","d"]],    "abcd", False), # "d" not adjacent to "c" here
            # TestCase([[???]], "???", ???),  # add your own
        ]
