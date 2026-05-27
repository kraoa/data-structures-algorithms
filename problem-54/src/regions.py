"""Read this first."""

import copy
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class TestCase:
    board: List[List[str]]           # 'X' or 'O'
    expected: List[List[str]]        # board after surrounded 'O' regions are flipped to 'X'


class Problem:
    """
    Given an m x n grid of 'X' and 'O', flip all 'O' cells that are fully
    surrounded by 'X' to 'X'. 'O' regions connected to the border are not flipped.

    Example:
        X X X X        X X X X
        X O O X   ->   X X X X
        X X O X        X X X X
        X O X X        X O X X   <- bottom O touches the border row, stays
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[List[str]], bool]]:
        """
        Passes a deep copy of each board to solver.solve(board).
        solver must expose .solve(board: List[List[str]]) -> None (modifies in place).
        Returns (test_case, modified_board, passed).
        """
        results = []
        for tc in self.test_cases:
            board = copy.deepcopy(tc.board)
            solver.solve(board)
            passed = board == tc.expected
            results.append((tc, board, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(                                           # LeetCode example
                board=[
                    ["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"],
                ],
                expected=[
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"],
                ],
            ),
            TestCase(board=[["X"]], expected=[["X"]]),          # single X
            TestCase(board=[["O"]], expected=[["O"]]),          # single O on border — stays
            TestCase(                                           # all O's touch border
                board=[["O", "X"], ["X", "O"]],
                expected=[["O", "X"], ["X", "O"]],
            ),
            TestCase(                                           # center O fully surrounded
                board=[
                    ["X", "X", "X"],
                    ["X", "O", "X"],
                    ["X", "X", "X"],
                ],
                expected=[
                    ["X", "X", "X"],
                    ["X", "X", "X"],
                    ["X", "X", "X"],
                ],
            ),
            # TestCase(board=[...], expected=[...]),  # add your own
        ]
