"""Read this first."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    n: int
    connections: List[List[int]]
    expected: List[List[int]]   # each bridge as sorted pair; list sorted


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                n=4,
                connections=[[0, 1], [1, 2], [2, 0], [1, 3]],
                expected=[[1, 3]],
            ),
            TestCase(n=2, connections=[[0, 1]], expected=[[0, 1]]),
            TestCase(n=3, connections=[[0, 1], [1, 2], [2, 0]], expected=[]),
            TestCase(
                n=5,
                connections=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]],
                expected=[[0, 1]],
            ),
            # TestCase(n=???, connections=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.critical_connections(
                tc.n, [list(e) for e in tc.connections]
            )
            actual_sorted = sorted(sorted(e) for e in actual)
            passed = actual_sorted == tc.expected
            results.append((tc, actual_sorted, passed))
        return results

    @staticmethod
    def brute_force(n: int, connections: List[List[int]]) -> List[List[int]]:
        """For each edge remove it and BFS-check if graph is still connected; O(E*(V+E))."""
        def is_connected(adj: dict, num_nodes: int) -> bool:
            if num_nodes == 0:
                return True
            visited = {0}
            queue = deque([0])
            while queue:
                node = queue.popleft()
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            return len(visited) == num_nodes

        bridges = []
        for idx, (u, v) in enumerate(connections):
            adj: dict[int, list[int]] = defaultdict(list)
            for i, (a, b) in enumerate(connections):
                if i != idx:
                    adj[a].append(b)
                    adj[b].append(a)
            if not is_connected(adj, n):
                bridges.append(sorted([u, v]))
        return sorted(bridges)
