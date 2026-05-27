"""Tests for the skip_list driver (Problem + Op). Must pass out of the box."""

import bisect
import unittest
from skip_list import Problem, Op


class ReferenceSkipList:
    """Reference implementation using a sorted Python list — O(n) per op."""

    def __init__(self) -> None:
        self._data: list = []

    def insert(self, val: int) -> None:
        bisect.insort(self._data, val)

    def search(self, val: int) -> bool:
        idx = bisect.bisect_left(self._data, val)
        return idx < len(self._data) and self._data[idx] == val

    def delete(self, val: int) -> None:
        idx = bisect.bisect_left(self._data, val)
        if idx < len(self._data) and self._data[idx] == val:
            self._data.pop(idx)


class TestSkipListDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            ref = ReferenceSkipList()
            for op in problem.ops:
                if op.kind == "insert":
                    ref.insert(op.val)
                elif op.kind == "delete":
                    ref.delete(op.val)
                else:
                    result = ref.search(op.val)
                    self.assertEqual(
                        op.expected,
                        result,
                        msg=f"search({op.val}): stored expected={op.expected}, brute force={result}",
                    )

    def test_run_returns_correct_structure(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(ReferenceSkipList)
            self.assertEqual(len(results), len(problem.ops))

    def test_run_passes_with_reference(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(ReferenceSkipList)
            for op, actual, passed in results:
                self.assertTrue(
                    passed,
                    msg=f"Reference failed on op={op}, actual={actual}",
                )


if __name__ == "__main__":
    unittest.main()
