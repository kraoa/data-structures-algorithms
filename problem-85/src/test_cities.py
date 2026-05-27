"""Tests for the Cities driver."""

import heapq
import math
import unittest
from typing import List

from cities import Cities, TestCase


def _dijkstra_all(n: int, edges: List[List[int]], threshold: int) -> int:
    """Run Dijkstra from each city, count reachable cities, return best city."""
    adj: List[List[tuple]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    def dijkstra(src: int) -> List[float]:
        dist = [math.inf] * n
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for w, v in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return dist

    best_city = -1
    best_count = math.inf
    for city in range(n):
        dist = dijkstra(city)
        count = sum(1 for other in range(n) if other != city and dist[other] <= threshold)
        if count <= best_count:
            best_count = count
            best_city = city
    return best_city


class TestCitiesDriver(unittest.TestCase):
    def test_expected_values_match_dijkstra(self) -> None:
        for tc in Cities.get_test_cases():
            result = _dijkstra_all(tc.n, tc.edges, tc.distance_threshold)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for n={tc.n}, threshold={tc.distance_threshold}",
            )


if __name__ == "__main__":
    unittest.main()
