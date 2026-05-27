"""
Runs your SkipList. It's useful to see how SkipList is called.
You may want to change how SkipList is constructed.
"""

from skip_list import Problem
from solver import SkipList


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}:")
        results = problem.run(SkipList)
        for op, actual, passed in results:
            if op.kind == "search":
                status = "PASS" if passed else "FAIL"
                print(
                    f"  search({op.val}) => {actual} "
                    f"(expected {op.expected}) [{status}]"
                )
            else:
                print(f"  {op.kind}({op.val})")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
