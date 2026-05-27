"""Read this first."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    edges: List[List[int]]
    expected: List[int]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(edges=[[1, 2], [1, 3], [2, 3]], expected=[2, 3]),
            TestCase(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], expected=[1, 4]),
            TestCase(edges=[[1, 2], [2, 3], [1, 3]], expected=[1, 3]),
            # TestCase(edges=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.find_redundant_connection([list(e) for e in tc.edges])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(edges: List[List[int]]) -> List[int]:
        """Add edges one by one; BFS-check if u,v are already connected before adding."""
        def connected(adj: dict, u: int, v: int) -> bool:
            visited = {u}
            queue = deque([u])
            while queue:
                node = queue.popleft()
                if node == v:
                    return True
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            return False

        adj: dict[int, list[int]] = defaultdict(list)
        result: List[int] = []
        for u, v in edges:
            if connected(adj, u, v):
                result = [u, v]
            adj[u].append(v)
            adj[v].append(u)
        return result
