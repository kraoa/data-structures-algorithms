"""Tests for Problem. Verifies stored expected values via a BFS/DFS reference."""

import unittest
from typing import List
from collections import defaultdict

from flights import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _bfs_reference(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """BFS layer by layer; each layer = one additional stop."""
        if src == dst:
            return 0
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0
        frontier = [(src, 0)]  # (city, cost)
        for _ in range(k + 1):
            next_frontier = []
            for city, cost in frontier:
                for neighbor, price in graph[city]:
                    if cost + price < dist[neighbor]:
                        dist[neighbor] = cost + price
                        next_frontier.append((neighbor, dist[neighbor]))
            frontier = next_frontier
        return dist[dst] if dist[dst] != INF else -1

    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._bfs_reference(tc.n, tc.flights, tc.src, tc.dst, tc.k)
            self.assertEqual(
                tc.expected, ref,
                f"n={tc.n}, src={tc.src}, dst={tc.dst}, k={tc.k}: stored={tc.expected}, bfs={ref}",
            )

    def test_bfs_unreachable(self) -> None:
        self.assertEqual(self._bfs_reference(3, [[0,1,100],[1,2,100]], 0, 2, 0), -1)

    def test_bfs_trivial_same_src_dst(self) -> None:
        self.assertEqual(self._bfs_reference(1, [], 0, 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
