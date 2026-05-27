"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from regions import Problem
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
    print(f"[{status}]")
    print(f"  input:    {tc.board}")
    print(f"  expected: {tc.expected}")
    print(f"  got:      {actual}")

banner("END CODE OUTPUT")
