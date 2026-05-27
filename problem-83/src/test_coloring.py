"""Tests for the Coloring driver."""

import unittest
from collections import deque
from typing import List

from coloring import Coloring, TestCase


def _bfs_bipartite(graph: List[List[int]]) -> bool:
    """BFS 2-coloring reference."""
    color = [-1] * len(graph)
    for start in range(len(graph)):
        if color[start] != -1:
            continue
        color[start] = 0
        queue: deque = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True


class TestColoringDriver(unittest.TestCase):
    def test_expected_values_match_reference(self) -> None:
        for tc in Coloring.get_test_cases():
            result = _bfs_bipartite(tc.graph)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for graph={tc.graph}",
            )

    def test_single_node_no_edges(self) -> None:
        self.assertTrue(_bfs_bipartite([[]]))

    def test_triangle_is_not_bipartite(self) -> None:
        self.assertFalse(_bfs_bipartite([[1, 2], [0, 2], [0, 1]]))


if __name__ == "__main__":
    unittest.main()
