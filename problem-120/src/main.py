"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from board import Board
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")
solver = Solver()
for tc, actual, passed in Board.run(solver):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] click={tc.click}")
    print("  expected: " + " | ".join(" ".join(row) for row in tc.expected))
    print("  actual:   " + " | ".join(" ".join(row) for row in actual))
banner("END CODE OUTPUT")
