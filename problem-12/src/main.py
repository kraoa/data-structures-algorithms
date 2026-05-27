"""
Runs your Solver against all test cases.
It's useful to see how Solver is called.
"""

from grid import Problem
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    problem = Problem(Problem.get_test_cases())
    solver = Solver()

    for tc, actual, passed in problem.run(solver):
        rows = len(tc.grid)
        cols = len(tc.grid[0]) if tc.grid else 0
        status = "PASS" if passed else f"FAIL (expected {tc.expected})"
        print(f"  {rows}×{cols} grid → {actual} islands  [{status}]")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
