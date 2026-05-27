"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from cache_ops import Problem
from solver import LFUCache


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for problem in Problem.get_test_cases():
        print(f"capacity={problem.capacity}")
        for op, actual, passed in problem.run(LFUCache):
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] get({op.key}) => got {actual}, expected {op.expected}")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
