"""Tests for Problem. Verifies stored expected values via a Bellman-Ford reference."""

import unittest
from typing import List

from graph import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _bellman_ford(times: List[List[int]], n: int, k: int) -> int:
        """O(V*E) Bellman-Ford reference — simpler to verify than Dijkstra."""
        INF = float("inf")
        dist = [INF] * (n + 1)
        dist[k] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        reachable = [dist[i] for i in range(1, n + 1)]
        if any(d == INF for d in reachable):
            return -1
        return max(reachable)

    def test_expected_values_match_bellman_ford(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._bellman_ford(tc.times, tc.n, tc.k)
            self.assertEqual(
                tc.expected, ref,
                f"times={tc.times}, n={tc.n}, k={tc.k}: stored={tc.expected}, bf={ref}",
            )

    def test_bellman_ford_unreachable(self) -> None:
        self.assertEqual(self._bellman_ford([[1, 2, 1]], 2, 2), -1)

    def test_bellman_ford_single_node(self) -> None:
        self.assertEqual(self._bellman_ford([], 1, 1), 0)


if __name__ == "__main__":
    unittest.main()
