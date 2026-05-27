"""You'll implement this."""

from typing import List, Optional

from board import Board, Move


class Solver:
    """Finds the shortest sequence of moves to reach the goal state."""

    def __init__(self, board: Board):
        self.board = board
        self.solution: Optional[List[Move]] = None

    def solve(self) -> None:
        pass

    def get_solution(self) -> Optional[List[Move]]:
        return self.solution
