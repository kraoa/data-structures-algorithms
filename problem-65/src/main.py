"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from booking import Problem
from solver import MyCalendarThree


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for problem in Problem.get_test_cases():
        for op, actual, passed in problem.run(MyCalendarThree):
            status = "PASS" if passed else "FAIL"
            print(
                f"  [{status}] book({op.start},{op.end}) => got {actual}, expected {op.expected}"
            )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
