"""Tests for the Nested driver."""

import unittest
from typing import List, Union

from nested import NestedInteger, Op, Problem


def _flatten(data: Union[int, list]) -> List[int]:
    """Recursively flatten a Python int or nested list to a flat list of ints."""
    if isinstance(data, int):
        return [data]
    result: List[int] = []
    for item in data:
        result.extend(_flatten(item))
    return result


def _expected_sequence(problem: Problem) -> List[int]:
    """Return the flat integer sequence the iterator should produce."""
    result: List[int] = []
    for item in problem.nested_list_data:
        result.extend(_flatten(item))
    return result


class TestNestedDriver(unittest.TestCase):
    def test_ops_match_flat_sequence(self) -> None:
        for problem in Problem.get_test_cases():
            flat = _expected_sequence(problem)
            next_values = [op.expected for op in problem.ops if op.kind == "next"]
            self.assertEqual(
                flat,
                next_values,
                msg=f"Flat sequence mismatch for {problem.nested_list_data}",
            )

    def test_nested_integer_from_list_integer(self) -> None:
        ni = NestedInteger.from_list(42)
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), 42)

    def test_nested_integer_from_list_nested(self) -> None:
        ni = NestedInteger.from_list([1, [2, 3]])
        self.assertFalse(ni.isInteger())
        children = ni.getList()
        self.assertEqual(len(children), 2)
        self.assertTrue(children[0].isInteger())
        self.assertEqual(children[0].getInteger(), 1)
        self.assertFalse(children[1].isInteger())

    def test_has_next_sequence_alternates_correctly(self) -> None:
        for problem in Problem.get_test_cases():
            kinds = [op.kind for op in problem.ops]
            # hasNext before each next, hasNext(False) at end
            for i, kind in enumerate(kinds):
                if kind == "next" and i > 0:
                    self.assertEqual(kinds[i - 1], "hasNext")


if __name__ == "__main__":
    unittest.main()
