"""Read this first."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    n: int
    edges: List[List[int]]
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(n=5, edges=[[0, 1], [1, 2], [3, 4]], expected=2),
            TestCase(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]], expected=1),
            TestCase(n=1, edges=[], expected=1),
            TestCase(n=4, edges=[], expected=4),
            TestCase(n=3, edges=[[0, 1], [1, 2], [0, 2]], expected=1),
            TestCase(n=6, edges=[[0, 1], [2, 3], [4, 5]], expected=3),
            # TestCase(n=???, edges=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.count_components(tc.n, [list(e) for e in tc.edges])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def bfs_count(n: int, edges: List[List[int]]) -> int:
        """BFS restart reference: O(V+E)."""
        adj: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        count = 0
        for start in range(n):
            if visited[start]:
                continue
            count += 1
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
        return count
