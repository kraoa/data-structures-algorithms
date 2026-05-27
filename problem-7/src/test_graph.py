"""Tests for Graph and Problem helpers."""

import unittest
from graph import Graph, Problem


class GraphTest(unittest.TestCase):

    def test_is_valid_order_simple(self) -> None:
        graph = Graph(2, [(1, 0)])
        self.assertTrue(graph.is_valid_order([0, 1]))
        self.assertFalse(graph.is_valid_order([1, 0]))  # prereq after dependent

    def test_is_valid_order_wrong_length(self) -> None:
        graph = Graph(3, [])
        self.assertFalse(graph.is_valid_order([0, 1]))

    def test_is_valid_order_wrong_labels(self) -> None:
        graph = Graph(2, [])
        self.assertFalse(graph.is_valid_order([0, 99]))

    def test_is_valid_order_no_prereqs(self) -> None:
        graph = Graph(3, [])
        # Every permutation of [0,1,2] is valid when there are no prereqs.
        self.assertTrue(graph.is_valid_order([0, 1, 2]))
        self.assertTrue(graph.is_valid_order([2, 1, 0]))
        self.assertTrue(graph.is_valid_order([1, 0, 2]))

    def test_has_cycle_true(self) -> None:
        self.assertTrue(Graph(2, [(1, 0), (0, 1)]).has_cycle())

    def test_has_cycle_false(self) -> None:
        self.assertFalse(Graph(4, [(1, 0), (2, 0), (3, 1), (3, 2)]).has_cycle())

    def test_has_cycle_single_course(self) -> None:
        self.assertFalse(Graph(1, []).has_cycle())

    def test_prereqs_of(self) -> None:
        graph = Graph(4, [(1, 0), (2, 0), (3, 1)])
        self.assertEqual(sorted(graph.prereqs_of(3)), [1])
        self.assertEqual(graph.prereqs_of(0), [])


if __name__ == "__main__":
    unittest.main()
