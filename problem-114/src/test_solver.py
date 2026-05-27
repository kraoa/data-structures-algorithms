"""Tests for IntervalTree solver. Assertions are commented out until implemented."""

import unittest
from interval_tree import Problem, Op
from solver import IntervalTree


class TestIntervalTreeSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(IntervalTree)

    # def test_basic_query(self) -> None:
    #     problem = Problem([
    #         Op("insert", 1, 5, None),
    #         Op("insert", 3, 8, None),
    #         Op("insert", 2, 4, None),
    #         Op("query", 4, None, 3),
    #     ])
    #     results = problem.run(IntervalTree)
    #     _, actual, passed = results[-1]
    #     self.assertTrue(passed, f"query(4) expected 3, got {actual}")

    # def test_no_containing_intervals(self) -> None:
    #     problem = Problem([
    #         Op("insert", 1, 3, None),
    #         Op("query", 5, None, 0),
    #     ])
    #     results = problem.run(IntervalTree)
    #     _, actual, passed = results[-1]
    #     self.assertTrue(passed)

    # def test_boundary_points(self) -> None:
    #     # Intervals are inclusive on both ends.
    #     problem = Problem([
    #         Op("insert", 5, 10, None),
    #         Op("query", 5, None, 1),
    #         Op("query", 10, None, 1),
    #         Op("query", 4, None, 0),
    #         Op("query", 11, None, 0),
    #     ])
    #     results = problem.run(IntervalTree)
    #     for op, actual, passed in results:
    #         if op.kind == "query":
    #             self.assertTrue(passed, f"query({op.lo}) expected {op.expected}, got {actual}")


if __name__ == "__main__":
    unittest.main()
