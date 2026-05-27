"""
Runs your IntervalTree. It's useful to see how IntervalTree is called.
You may want to change how IntervalTree is constructed.
"""

from interval_tree import Problem
from solver import IntervalTree


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}:")
        results = problem.run(IntervalTree)
        for op, actual, passed in results:
            if op.kind == "insert":
                print(f"  insert({op.lo}, {op.hi})")
            else:
                status = "PASS" if passed else "FAIL"
                print(
                    f"  query({op.lo}) => {actual} "
                    f"(expected {op.expected}) [{status}]"
                )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
