"""Tests for the reachability driver. Must pass out of the box."""

import unittest
from collections import deque
from typing import List

from reachability import Problem, TestCase


def _brute_force(graph: List[List[int]]) -> int:
    """BFS with frozenset-visited state — same idea as bitmask BFS, clearly different code."""
    n = len(graph)
    if n == 1:
        return 0
    full = frozenset(range(n))
    q: deque = deque()
    seen = set()
    for s in range(n):
        state = (s, frozenset([s]))
        q.append((s, frozenset([s]), 0))
        seen.add(state)
    while q:
        node, visited, dist = q.popleft()
        for nb in graph[node]:
            nv = visited | {nb}
            if nv == full:
                return dist + 1
            state = (nb, nv)
            if state not in seen:
                seen.add(state)
                q.append((nb, nv, dist + 1))
    return -1  # unreachable for connected graphs


class TestReachabilityDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.graph)
            self.assertEqual(
                tc.expected,
                bf,
                msg=f"graph={tc.graph}: stored={tc.expected}, brute force={bf}",
            )

    def test_run_returns_correct_structure(self) -> None:
        class _ZeroSolver:
            def shortest_path_length(self, graph):
                return 0

        results = Problem.run(_ZeroSolver())
        self.assertEqual(len(results), len(Problem.get_test_cases()))
        for tc, actual, passed in results:
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
