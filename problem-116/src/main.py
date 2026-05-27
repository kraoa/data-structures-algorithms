"""
Runs your AVLTree. It's useful to see how AVLTree is called.
You may want to change how AVLTree is constructed.
"""

from avl_tree import Problem
from solver import AVLTree


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}:")
        results = problem.run(AVLTree)
        for op, actual, passed in results:
            if op.kind == "insert":
                print(f"  insert({op.val})")
            else:
                status = "PASS" if passed else "FAIL"
                print(
                    f"  {op.kind}({op.val!r}) => {actual!r} "
                    f"(expected {op.expected!r}) [{status}]"
                )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
