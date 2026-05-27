"""
Runs your MedianFinder against all test cases.
It's useful to see how MedianFinder is called.
"""

from stream import Problem
from solver import MedianFinder


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    for i, problem in enumerate(Problem.get_test_cases()):
        finder = MedianFinder()
        results = problem.run(finder)

        passed_all = all(passed for _, _, passed in results)
        print(f"\nTest {i + 1}: {'PASS' if passed_all else 'FAIL'}")
        for op, actual, passed in results:
            status = "OK" if passed else f"WRONG — expected {op.expected}"
            print(f"  {op} → got {actual}  [{status}]")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
