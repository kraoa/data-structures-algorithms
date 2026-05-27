"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    points: List[List[int]]
    expected: int


class Collinear:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1,1],[2,2],[3,3]], 3),
            TestCase([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),
            TestCase([[0,0]], 1),
            TestCase([[0,0],[1,1]], 2),
            TestCase([[0,0],[1,1],[0,0]], 3),
            # TestCase("???", ??),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Collinear.get_test_cases():
            actual = solver.max_points([list(p) for p in tc.points])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
