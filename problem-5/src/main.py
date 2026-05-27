"""
Runs your Serializer against all test cases.
It's useful to see how Serializer is called.
"""

from tree import Problem, to_list
from solver import Serializer


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    serializer = Serializer()
    for i, problem in enumerate(Problem.get_test_cases()):
        passed = problem.check(serializer)
        encoded = serializer.serialize(problem.root)
        print(f"\nTest {i + 1}: {'PASS' if passed else 'FAIL'}")
        print(f"  original: {problem.values}")
        print(f"  encoded:  {repr(encoded)}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
