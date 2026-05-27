"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from word_pairs import Problem
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    solver = Solver()
    for i, (tc, actual, passed) in enumerate(Problem.run(solver)):
        status = "PASS" if passed else "FAIL"
        print(f"\nCase {i + 1}: words={tc.words}")
        print(f"  expected : {sorted(tc.expected)}")
        print(f"  actual   : {sorted(actual)}")
        print(f"  [{status}]")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
