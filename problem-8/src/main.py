"""
Runs your Solver against all test cases.
It's useful to see how Solver is called.
"""

from segmentation import Problem
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
        status = "PASS" if passed else "FAIL"
        print(f"\n  s={repr(tc.s)}  [{status}]")
        print(f"  got:      {sorted(actual)}")
        if not passed:
            print(f"  expected: {sorted(tc.expected)}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
