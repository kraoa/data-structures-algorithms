"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from interleaving import Problem
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
    print(f"[{status}] s1={tc.s1!r:8} s2={tc.s2!r:8} s3={tc.s3!r:15} expected={tc.expected!r:6} got={actual!r}")

banner("END CODE OUTPUT")
