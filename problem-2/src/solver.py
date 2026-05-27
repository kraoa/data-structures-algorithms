"""You'll implement this."""

from typing import List

from puzzle import Puzzle


class Solver:
    """Solves Mastermind puzzles."""

    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.guesses: List[List[int]] = []

    def solve_puzzle(self) -> None:
        pass

    def get_guesses(self) -> List[List[int]]:
        return self.guesses
