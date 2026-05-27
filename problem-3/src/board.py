"""Read this first."""

from enum import Enum
from typing import List, Tuple


class Move(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


# Goal: tiles 1-8 in order, blank (0) at bottom-right.
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


class Board:
    """
    Represents a 3x3 sliding-tile puzzle (the 8-puzzle).

    Tiles are stored as a flat tuple of 9 integers. 0 is the blank.
    Moves slide the blank in the given direction.

    Example layout (indices):
        0 1 2
        3 4 5
        6 7 8
    """

    SIZE = 3

    def __init__(self, tiles: Tuple[int, ...]):
        if len(tiles) != self.SIZE * self.SIZE:
            raise ValueError(f"expected {self.SIZE * self.SIZE} tiles, got {len(tiles)}")
        if sorted(tiles) != list(range(self.SIZE * self.SIZE)):
            raise ValueError("tiles must contain exactly the integers 0 through 8")
        self._tiles = tuple(tiles)
        self._moves: List[Move] = []

    def tiles(self) -> Tuple[int, ...]:
        return self._tiles

    def is_solved(self) -> bool:
        return self._tiles == GOAL_STATE

    def blank_pos(self) -> Tuple[int, int]:
        """Returns (row, col) of the blank tile."""
        idx = self._tiles.index(0)
        return idx // self.SIZE, idx % self.SIZE

    def valid_moves(self) -> List[Move]:
        """Returns moves that keep the blank inside the grid."""
        row, col = self.blank_pos()
        moves = []
        if row > 0:
            moves.append(Move.UP)
        if row < self.SIZE - 1:
            moves.append(Move.DOWN)
        if col > 0:
            moves.append(Move.LEFT)
        if col < self.SIZE - 1:
            moves.append(Move.RIGHT)
        return moves

    def apply_move(self, move: Move) -> "Board":
        """Returns a new Board after sliding the blank in the given direction."""
        if move not in self.valid_moves():
            raise ValueError(f"{move} is not valid from this position")

        row, col = self.blank_pos()
        blank_idx = row * self.SIZE + col

        delta = {
            Move.UP: -self.SIZE,
            Move.DOWN: self.SIZE,
            Move.LEFT: -1,
            Move.RIGHT: 1,
        }
        other_idx = blank_idx + delta[move]

        tiles = list(self._tiles)
        tiles[blank_idx], tiles[other_idx] = tiles[other_idx], tiles[blank_idx]

        new_board = Board(tuple(tiles))
        new_board._moves = self._moves + [move]
        return new_board

    def move_history(self) -> List[Move]:
        """Returns the sequence of moves applied to reach this board from its origin."""
        return list(self._moves)

    def is_solvable(self) -> bool:
        """
        Returns True if this configuration can reach GOAL_STATE.

        For an odd-width grid (3x3): a configuration is solvable iff the
        number of inversions among non-blank tiles is even.
        """
        tiles = [t for t in self._tiles if t != 0]
        inversions = 0
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] > tiles[j]:
                    inversions += 1
        return inversions % 2 == 0

    def display(self) -> str:
        rows = []
        for r in range(self.SIZE):
            row_tiles = self._tiles[r * self.SIZE : (r + 1) * self.SIZE]
            rows.append(" ".join(str(t) if t != 0 else "_" for t in row_tiles))
        return "\n".join(rows)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Board) and self._tiles == other._tiles

    def __hash__(self) -> int:
        return hash(self._tiles)
