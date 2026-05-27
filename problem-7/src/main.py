"""
Runs your Solver against all test graphs.
It's useful to see how Solver is called.
"""

from graph import Problem
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

    for graph, order, passed in problem.run(solver):
        status = "PASS" if passed else "FAIL"
        note = " (cycle)" if graph.has_cycle() else ""
        print(
            f"  {graph.num_courses} courses, prereqs={graph.prerequisites}{note}"
            f" → {order}  [{status}]"
        )

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
