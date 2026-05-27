"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    graph: List[List[int]]
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(graph=[[1, 2, 3], [0], [0], [0]], expected=4),
            TestCase(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], expected=4),
            TestCase(graph=[[1], [0]], expected=1),
            TestCase(graph=[[1, 2], [0, 2], [0, 1]], expected=2),
            # TestCase(graph=[[???]], expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Problem.get_test_cases():
            # Pass a deep copy so stored test cases are never modified.
            import copy
            actual = solver.shortest_path_length(copy.deepcopy(tc.graph))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
