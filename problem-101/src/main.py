"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from shuffling import Shuffling
from solver import Solution


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

for prob, op_results, all_passed in Shuffling.run(Solution):
    print(f"nums={prob.nums}")
    for op, actual, passed in op_results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {op.kind}: actual={actual}")

banner("END CODE OUTPUT")
