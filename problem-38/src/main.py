"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from alphabet import Problem
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
        if not tc.possible:
            expected_str = '""'
        else:
            expected_str = f"(valid {tc.n_chars}-char order)"
        print(f"  words={tc.words} → {actual!r}  [expected {expected_str}] [{status}]")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
