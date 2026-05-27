"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from ordering import Ordering
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

solver = Solver()
for tc, actual, passed in Ordering.run(solver):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] nums={tc.nums} expected={tc.expected!r} actual={actual!r}")

banner("END CODE OUTPUT")
