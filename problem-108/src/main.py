"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from hashmap import HashMap
from solver import MyHashMap


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


banner("BEGIN CODE OUTPUT")

for prob, op_results, all_passed in HashMap.run(MyHashMap):
    for op, actual, passed in op_results:
        if op.kind == "get":
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] get({op.key}) expected={op.expected} actual={actual}")
        else:
            print(f"  [----] {op.kind}({op.key}{', ' + str(op.value) if op.value is not None else ''})")

banner("END CODE OUTPUT")
