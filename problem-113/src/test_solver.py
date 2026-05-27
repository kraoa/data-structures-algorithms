"""Tests for SkipList solver. Assertions are commented out until implemented."""

import unittest
from skip_list import Problem, Op
from solver import SkipList


class TestSkipListSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(SkipList)

    # def test_basic_search(self) -> None:
    #     problem = Problem([
    #         Op("insert", 5, None),
    #         Op("search", 5, True),
    #         Op("search", 3, False),
    #     ])
    #     results = problem.run(SkipList)
    #     for op, actual, passed in results:
    #         if op.kind == "search":
    #             self.assertTrue(passed, f"search({op.val}) expected {op.expected}, got {actual}")

    # def test_delete_then_search(self) -> None:
    #     problem = Problem([
    #         Op("insert", 10, None),
    #         Op("delete", 10, None),
    #         Op("search", 10, False),
    #     ])
    #     results = problem.run(SkipList)
    #     _, actual, passed = results[-1]
    #     self.assertTrue(passed)

    # def test_delete_nonexistent(self) -> None:
    #     # Deleting a value never inserted should not raise and should leave state consistent.
    #     sl = SkipList()
    #     sl.delete(99)
    #     self.assertFalse(sl.search(99))


if __name__ == "__main__":
    unittest.main()
