"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from collections import Counter
from weighted import Weighted
from solver import Solution


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

for prob, picks, passed in Weighted.run(Solution):
    status = "PASS" if passed else "FAIL"
    freq = Counter(picks)
    print(f"[{status}] w={prob.w} trials={prob.trials} freq={dict(sorted(freq.items()))}")

banner("END CODE OUTPUT")
