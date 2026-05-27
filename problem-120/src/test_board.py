import copy
import unittest
from collections import deque
from typing import List, Tuple

from board import Board, TestCase


class TestBoard(unittest.TestCase):
    @staticmethod
    def _reveal(board: List[List[str]], click: Tuple[int, int]) -> List[List[str]]:
        """BFS reference — O(rows * cols)."""
        rows, cols = len(board), len(board[0])
        r, c = click

        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        def adj_mines(row: int, col: int) -> int:
            return sum(
                board[row + dr][col + dc] == "M"
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr or dc) and 0 <= row + dr < rows and 0 <= col + dc < cols
            )

        queue: deque = deque([(r, c)])
        visited = {(r, c)}
        while queue:
            r, c = queue.popleft()
            mines = adj_mines(r, c)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = "B"
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if not (dr or dc):
                            continue
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and board[nr][nc] == "E"
                        ):
                            visited.add((nr, nc))
                            queue.append((nr, nc))
        return board

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Board.get_test_cases():
            result = self._reveal(copy.deepcopy(tc.board), tc.click)
            self.assertEqual(tc.expected, result)


if __name__ == "__main__":
    unittest.main()
