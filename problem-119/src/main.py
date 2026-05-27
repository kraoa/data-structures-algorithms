"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from stations import Problem
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    solver = Solver()
    for tc, actual, passed in Problem.run(solver):
        status = "PASS" if passed else "FAIL"
        print(
            f"  vehicles={tc.vehicles} => {actual} "
            f"(expected {tc.expected}) [{status}]"
        )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
