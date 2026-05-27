"""Tests for the sparse_table driver (Problem + Op). Must pass out of the box."""

import unittest
from sparse_table import Problem, Op


class NaiveSparseTable:
    """O(n) per query reference — obviously correct."""

    def __init__(self, nums: list) -> None:
        self.nums = nums

    def query(self, left: int, right: int) -> int:
        return min(self.nums[left : right + 1])


class TestSparseTableDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            naive = NaiveSparseTable(problem.nums)
            for op in problem.ops:
                expected_naive = naive.query(op.left, op.right)
                self.assertEqual(
                    op.expected,
                    expected_naive,
                    msg=(
                        f"nums={problem.nums} query({op.left},{op.right}): "
                        f"stored expected={op.expected}, brute force={expected_naive}"
                    ),
                )

    def test_run_returns_correct_structure(self) -> None:
        """run() returns (op, actual, passed) tuples — one per op."""
        for problem in Problem.get_test_cases():
            results = problem.run(NaiveSparseTable)
            self.assertEqual(len(results), len(problem.ops))
            for (op, actual, passed), orig_op in zip(results, problem.ops):
                self.assertIs(op, orig_op)
                self.assertIsInstance(passed, bool)

    def test_run_does_not_mutate_stored_nums(self) -> None:
        problem = Problem.get_test_cases()[0]
        original = list(problem.nums)
        problem.run(NaiveSparseTable)
        self.assertEqual(problem.nums, original)


if __name__ == "__main__":
    unittest.main()
