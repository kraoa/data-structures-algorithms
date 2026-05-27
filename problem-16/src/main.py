"""
Runs your Solver against all test cases.
It's useful to see how Solver is called.
"""

from board import Problem
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

    for tc, solutions, passed in problem.run(solver):
        status = "PASS" if passed else f"FAIL (expected {tc.expected_count} solutions)"
        print(f"\n  n={tc.n}: found {len(solutions)} solutions  [{status}]")
        for sol in solutions[:2]:  # show first two to keep output manageable
            for row in sol:
                print(f"    {row}")
            print()

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
