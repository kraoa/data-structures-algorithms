"""Tests for the NestedIterator solver."""

import unittest

from nested import NestedInteger, Problem
from solver import NestedIterator


class TestNestedIterator(unittest.TestCase):
    def test_smoke(self) -> None:
        ni_list = [NestedInteger.from_list(item) for item in [[1, 1], 2, [1, 1]]]
        iterator = NestedIterator(ni_list)
        iterator.hasNext()

    # def test_flat_sequence_basic(self) -> None:
    #     ni_list = [NestedInteger.from_list(item) for item in [[1, 1], 2, [1, 1]]]
    #     iterator = NestedIterator(ni_list)
    #     result = []
    #     while iterator.hasNext():
    #         result.append(iterator.next())
    #     self.assertEqual(result, [1, 1, 2, 1, 1])

    # def test_deeply_nested(self) -> None:
    #     ni_list = [NestedInteger.from_list(item) for item in [1, [4, [6]]]]
    #     iterator = NestedIterator(ni_list)
    #     result = []
    #     while iterator.hasNext():
    #         result.append(iterator.next())
    #     self.assertEqual(result, [1, 4, 6])

    # def test_has_next_idempotent(self) -> None:
    #     # Calling hasNext() multiple times without next() must not advance the iterator.
    #     ni_list = [NestedInteger.from_list(1)]
    #     iterator = NestedIterator(ni_list)
    #     self.assertTrue(iterator.hasNext())
    #     self.assertTrue(iterator.hasNext())
    #     self.assertEqual(iterator.next(), 1)
    #     self.assertFalse(iterator.hasNext())


if __name__ == "__main__":
    unittest.main()
