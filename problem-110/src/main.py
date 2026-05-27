"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from expressions import Expressions
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

solver = Solver()
for tc, actual, passed in Expressions.run(solver):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] num={tc.num!r} target={tc.target}")
    print(f"        expected={sorted(tc.expected)}")
    print(f"        actual  ={actual}")

banner("END CODE OUTPUT")
