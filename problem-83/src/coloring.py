"""Read this first."""

from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    graph: List[List[int]]
    expected: bool


class Coloring:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
            TestCase([[1, 3], [0, 2], [1, 3], [0, 2]], True),
            TestCase([[1], [0], [3], [2]], True),
            TestCase([[]], True),
            TestCase([[1, 3], [0, 2], [1, 3], [0, 2], [5], [4]], True),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, bool, bool]]:
        results = []
        for tc in Coloring.get_test_cases():
            actual = solver.is_bipartite(copy.deepcopy(tc.graph))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
