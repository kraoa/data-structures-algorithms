"""
Runs your Trie against all test problems.
It's useful to see how Trie is called.
"""

from words import Problem
from solver import Trie


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    for i, problem in enumerate(Problem.get_test_cases()):
        results = problem.run(Trie)
        passed_all = all(passed for _, _, passed in results)
        print(f"\nTest {i + 1}: {'PASS' if passed_all else 'FAIL'}")
        for op, actual, passed in results:
            status = "OK" if passed else f"WRONG — expected {op.expected}"
            print(f"  {op} → got {actual}  [{status}]")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
