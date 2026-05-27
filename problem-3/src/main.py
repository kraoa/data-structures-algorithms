"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

import os
from typing import List, Tuple

from board import Board
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def load_puzzles(filepath: str) -> List[Tuple[int, ...]]:
    """Load puzzle configs from a file. Each non-comment line is 9 space-separated ints."""
    puzzles = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                tiles: Tuple[int, ...] = tuple(int(x) for x in line.split())
                puzzles.append(tiles)
    return puzzles


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    puzzle_file = os.path.join("data", "puzzles.txt")
    puzzles = load_puzzles(puzzle_file)

    for i, tiles in enumerate(puzzles):
        board = Board(tiles)
        print(f"\nPuzzle {i + 1}:")
        print(board.display())

        if not board.is_solvable():
            print("  Not solvable!")
            continue

        solver = Solver(board)
        solver.solve()

        solution = solver.get_solution()
        if solution is not None:
            print(f"  Solved in {len(solution)} moves: {[m.value for m in solution]}")
        else:
            print("  No solution found.")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
