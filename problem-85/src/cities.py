"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    n: int
    edges: List[List[int]]
    distance_threshold: int
    expected: int


class Cities:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
            TestCase(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0),
            TestCase(2, [[0, 1, 1]], 1, 1),
            TestCase(3, [[0, 1, 5], [1, 2, 5]], 3, 2),
            # TestCase("???", "??", "??", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Cities.get_test_cases():
            actual = solver.find_the_city(tc.n, [e[:] for e in tc.edges], tc.distance_threshold)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
