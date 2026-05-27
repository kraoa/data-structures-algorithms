"""
Runs your SparseTable. It's useful to see how SparseTable is called.
You may want to change how SparseTable is constructed.
"""

from sparse_table import Problem
from solver import SparseTable


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}: nums={problem.nums}")
        results = problem.run(SparseTable)
        for op, actual, passed in results:
            status = "PASS" if passed else "FAIL"
            print(
                f"  query({op.left}, {op.right}) => {actual} "
                f"(expected {op.expected}) [{status}]"
            )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
