"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    board: List[List[str]]
    click: Tuple[int, int]
    expected: List[List[str]]


class Board:
    """
    Minesweeper board cells:
      'M' — unrevealed mine
      'E' — unrevealed empty
      'B' — revealed blank (no adjacent mines)
      'X' — revealed mine (game over)
      '1'–'8' — revealed with adjacent mine count
    """

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                board=[
                    ["E", "E", "E", "E", "E"],
                    ["E", "E", "M", "E", "E"],
                    ["E", "E", "E", "E", "E"],
                    ["E", "E", "E", "E", "E"],
                ],
                click=(3, 0),
                expected=[
                    ["B", "1", "E", "1", "B"],
                    ["B", "1", "M", "1", "B"],
                    ["B", "1", "1", "1", "B"],
                    ["B", "B", "B", "B", "B"],
                ],
            ),
            TestCase(
                board=[
                    ["B", "1", "E", "1", "B"],
                    ["B", "1", "M", "1", "B"],
                    ["B", "1", "1", "1", "B"],
                    ["B", "B", "B", "B", "B"],
                ],
                click=(1, 2),
                expected=[
                    ["B", "1", "E", "1", "B"],
                    ["B", "1", "X", "1", "B"],
                    ["B", "1", "1", "1", "B"],
                    ["B", "B", "B", "B", "B"],
                ],
            ),
            TestCase(
                board=[["M"]],
                click=(0, 0),
                expected=[["X"]],
            ),
            TestCase(
                board=[["E"]],
                click=(0, 0),
                expected=[["B"]],
            ),
            TestCase(
                board=[
                    ["E", "M"],
                    ["E", "E"],
                ],
                click=(1, 1),
                expected=[
                    ["E", "M"],
                    ["E", "1"],
                ],
            ),
            # TestCase([["???", "???"]], (0, 0), [["???", "???"]]),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[List[str]], bool]]:
        results = []
        for tc in Board.get_test_cases():
            actual = solver.update(copy.deepcopy(tc.board), tc.click)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
