"""Tests for Problem. Verifies stored expected values via a reference DFS."""

import unittest
import copy
from typing import List

from grid import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _dfs(board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = any(backtrack(r + dr, c + dc, idx + 1)
                        for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)))
            board[r][c] = tmp
            return found

        return any(backtrack(r, c, 0) for r in range(m) for c in range(n))

    def test_expected_values_match_dfs(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._dfs(copy.deepcopy(tc.board), tc.word)
            self.assertEqual(
                tc.expected, ref,
                f"word={tc.word!r}: stored={tc.expected}, dfs={ref}",
            )

    def test_dfs_single_cell(self) -> None:
        self.assertTrue(self._dfs([["a"]], "a"))
        self.assertFalse(self._dfs([["a"]], "b"))

    def test_dfs_no_revisit(self) -> None:
        # "aaa" cannot be found in a 1×2 board ["a","a"] without revisiting.
        self.assertFalse(self._dfs([["a", "a"]], "aaa"))


if __name__ == "__main__":
    unittest.main()
