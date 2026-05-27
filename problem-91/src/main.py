"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from view import Problem
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

solver = Solver()
for tc, actual, passed in Problem(Problem.get_test_cases()).run(solver):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] values={tc.values!r:35} expected={tc.expected!r:12} got={actual!r}")

banner("END CODE OUTPUT")
