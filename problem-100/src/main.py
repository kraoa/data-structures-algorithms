"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from reservoir import Reservoir
from solver import Solution


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

for prob, msg, passed in Reservoir.run(Solution):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] values={prob.values} trials={prob.trials} msg={msg}")

banner("END CODE OUTPUT")
