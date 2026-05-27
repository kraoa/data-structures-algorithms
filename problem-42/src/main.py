"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from formatting import Problem
from solver import Solver


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    problem = Problem(Problem.get_test_cases())
    solver = Solver()

    for i, (tc, actual, passed) in enumerate(problem.run(solver)):
        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i + 1} (max_width={tc.max_width}):  [{status}]")
        for j, line in enumerate(actual):
            exp = tc.expected[j] if j < len(tc.expected) else "<missing>"
            match = "✓" if line == exp else "✗"
            print(f"  {match} |{line}|")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
