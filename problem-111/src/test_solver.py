"""Tests for SparseTable solver. Assertions are commented out until implemented."""

import unittest
from sparse_table import Problem, Op
from solver import SparseTable


class TestSparseTableSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(SparseTable)

    # def test_basic_query(self) -> None:
    #     problem = Problem([2, 4, 3, 1, 6, 7, 8, 9, 1, 7], [Op(0, 3, 1)])
    #     results = problem.run(SparseTable)
    #     _, actual, passed = results[0]
    #     self.assertTrue(passed, f"query(0,3) expected 1, got {actual}")

    # def test_single_element(self) -> None:
    #     problem = Problem([42], [Op(0, 0, 42)])
    #     results = problem.run(SparseTable)
    #     _, _, passed = results[0]
    #     self.assertTrue(passed)

    # def test_full_range(self) -> None:
    #     # Minimum is not at either endpoint — tests internal lookup
    #     problem = Problem([5, 3, 8, 1, 7], [Op(0, 4, 1)])
    #     results = problem.run(SparseTable)
    #     _, actual, passed = results[0]
    #     self.assertTrue(passed, f"query(0,4) expected 1, got {actual}")


if __name__ == "__main__":
    unittest.main()
