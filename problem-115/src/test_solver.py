"""Tests for FreqStack. Assertions are commented out until implemented."""

import unittest
from freq_stack import Problem, Op
from solver import FreqStack


class TestFreqStackSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(FreqStack)

    # def test_lc_example(self) -> None:
    #     problem = Problem([
    #         Op("push", 5, None), Op("push", 7, None), Op("push", 5, None),
    #         Op("push", 7, None), Op("push", 4, None), Op("push", 5, None),
    #         Op("pop", None, 5),
    #         Op("pop", None, 7),
    #         Op("pop", None, 5),
    #         Op("pop", None, 4),
    #     ])
    #     results = problem.run(FreqStack)
    #     for op, actual, passed in results:
    #         if op.kind == "pop":
    #             self.assertTrue(passed, f"pop() expected {op.expected}, got {actual}")

    # def test_tie_broken_by_recency(self) -> None:
    #     # After two pushes of 1 and one pop, push 2; both have freq 1 but 2 is more recent.
    #     problem = Problem([
    #         Op("push", 1, None), Op("push", 1, None),
    #         Op("pop", None, 1),
    #         Op("push", 2, None),
    #         Op("pop", None, 2),
    #         Op("pop", None, 1),
    #     ])
    #     results = problem.run(FreqStack)
    #     for op, actual, passed in results:
    #         if op.kind == "pop":
    #             self.assertTrue(passed, f"pop() expected {op.expected}, got {actual}")


if __name__ == "__main__":
    unittest.main()
