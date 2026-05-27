"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from counting import Counting
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    solver = Solver()
    banner("BEGIN CODE OUTPUT")
    for tc, actual, passed in Counting.run(solver):
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] s={tc.s!r}, t={tc.t!r} => {actual} (expected {tc.expected})")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
