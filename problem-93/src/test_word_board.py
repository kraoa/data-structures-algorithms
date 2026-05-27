"""Tests for the WordBoard driver (must pass out of the box)."""

import unittest
import copy
from typing import List
from word_board import WordBoard, TestCase


def _word_exists(board: List[List[str]], word: str) -> bool:
    """Standalone DFS — checks if a single word exists in the board."""
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        tmp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
        board[r][c] = tmp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


def _brute_find_words(board: List[List[str]], words: List[str]) -> List[str]:
    return sorted(w for w in words if _word_exists(copy.deepcopy(board), w))


class TestWordBoard(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in WordBoard.get_test_cases():
            brute = _brute_find_words(copy.deepcopy(tc.board), list(tc.words))
            self.assertEqual(sorted(tc.expected), brute)

    def test_no_cell_reuse(self) -> None:
        # "aaa" cannot be found in ["a","a"] because cells can't be reused.
        tc = WordBoard.get_test_cases()[3]
        brute = _brute_find_words(copy.deepcopy(tc.board), list(tc.words))
        self.assertEqual(brute, [])


if __name__ == "__main__":
    unittest.main()
