"""
Runs your FreqStack. It's useful to see how FreqStack is called.
You may want to change how FreqStack is constructed.
"""

from freq_stack import Problem
from solver import FreqStack


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}:")
        results = problem.run(FreqStack)
        for op, actual, passed in results:
            if op.kind == "push":
                print(f"  push({op.val})")
            else:
                status = "PASS" if passed else "FAIL"
                print(
                    f"  pop() => {actual} "
                    f"(expected {op.expected}) [{status}]"
                )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
