"""Tests for the rb_tree driver. Must pass out of the box."""

import unittest
from rb_tree import Problem, Op


class SortedListTree:
    """Reference using a sorted Python list — obviously correct."""

    def __init__(self) -> None:
        self._data: list = []

    def insert(self, val: int) -> None:
        if val not in self._data:
            self._data.append(val)
            self._data.sort()

    def search(self, val: int) -> bool:
        return val in self._data

    def inorder(self) -> list:
        return list(self._data)


class TestRBTreeDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            ref = SortedListTree()
            for op in problem.ops:
                if op.kind == "insert":
                    ref.insert(op.val)
                elif op.kind == "search":
                    result = ref.search(op.val)
                    self.assertEqual(
                        op.expected,
                        result,
                        msg=f"search({op.val}): stored expected={op.expected}, brute force={result}",
                    )
                else:  # inorder
                    result = ref.inorder()
                    self.assertEqual(
                        op.expected,
                        result,
                        msg=f"inorder: stored expected={op.expected}, brute force={result}",
                    )

    def test_run_returns_correct_structure(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(SortedListTree)
            self.assertEqual(len(results), len(problem.ops))

    def test_run_passes_with_reference(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(SortedListTree)
            for op, actual, passed in results:
                self.assertTrue(passed, msg=f"Reference failed: op={op}, actual={actual}")


if __name__ == "__main__":
    unittest.main()
