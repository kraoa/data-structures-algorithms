"""Tests for the Problem driver (components.py)."""

import unittest
from components import Problem


class TestComponents(unittest.TestCase):
    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.bfs_count(tc.n, tc.edges),
                msg=f"n={tc.n} edges={tc.edges}",
            )

    def test_single_node_no_edges(self) -> None:
        self.assertEqual(Problem.bfs_count(1, []), 1)

    def test_all_isolated(self) -> None:
        self.assertEqual(Problem.bfs_count(4, []), 4)

    def test_fully_connected(self) -> None:
        edges = [[0, 1], [1, 2], [2, 3]]
        self.assertEqual(Problem.bfs_count(4, edges), 1)


if __name__ == "__main__":
    unittest.main()
