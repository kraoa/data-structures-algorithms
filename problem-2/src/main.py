"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from puzzle import Puzzle
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    puzzle = Puzzle()  # random secret; pass a string like "1234" to fix the secret
    solver = Solver(puzzle)
    solver.solve_puzzle()

    for guess in solver.get_guesses():
        print(guess)
    if puzzle.won():
        print(f"WIN in {puzzle.num_guesses()}!")
    else:
        print(f"LOSS! It was '{puzzle.admit_defeat()}'")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
