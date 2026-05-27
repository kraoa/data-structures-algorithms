"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from spans import Problem
from solver import StockSpanner


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"--- Problem {i + 1} ---")
        for op, actual, passed in problem.run(StockSpanner):
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] next({op.price}) => {actual} (expected {op.expected})")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
