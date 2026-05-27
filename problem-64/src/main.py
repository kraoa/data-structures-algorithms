"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from range_queries import Problem
from solver import NumArray


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for problem in Problem.get_test_cases():
        print(f"nums={problem.nums}")
        for op, actual, passed in problem.run(NumArray):
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] sum_range({op.i},{op.j}) => got {actual}, expected {op.expected}")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
