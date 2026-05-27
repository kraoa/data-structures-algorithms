"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from nested import Problem
from solver import NestedIterator


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"--- Problem {i + 1}: {problem.nested_list_data} ---")
        for op, actual, passed in problem.run(NestedIterator):
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] {op.kind}() => {actual} (expected {op.expected})")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
