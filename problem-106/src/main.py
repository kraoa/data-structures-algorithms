"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from scheduling import Scheduling
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

solver = Solver()
for tc, actual, passed in Scheduling.run(solver):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] courses={tc.courses} expected={tc.expected} actual={actual}")

banner("END CODE OUTPUT")
