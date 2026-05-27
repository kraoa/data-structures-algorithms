"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    points: List[List[int]]
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], expected=20),
            TestCase(points=[[3, 12], [-2, 5], [-4, 1]], expected=18),
            TestCase(points=[[0, 0], [1, 1], [1, 0], [0, 1]], expected=3),
            TestCase(points=[[0, 0]], expected=0),
            # TestCase(points=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.min_cost_connect_points([list(p) for p in tc.points])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _manhattan(a: List[int], b: List[int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def brute_force_prim(points: List[List[int]]) -> int:
        """O(n^2) Prim's without a heap — find min edge by scanning unvisited nodes."""
        n = len(points)
        if n == 1:
            return 0
        INF = float("inf")
        dist = [INF] * n
        dist[0] = 0
        in_mst = [False] * n
        total = 0
        for _ in range(n):
            # Pick the unvisited node with the smallest dist to the current MST.
            u = min(
                (i for i in range(n) if not in_mst[i]),
                key=lambda i: dist[i],
            )
            in_mst[u] = True
            total += dist[u]
            for v in range(n):
                if not in_mst[v]:
                    d = Problem._manhattan(points[u], points[v])
                    if d < dist[v]:
                        dist[v] = d
        return total
