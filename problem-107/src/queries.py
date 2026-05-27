"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    intervals: List[List[int]]
    queries: List[int]
    expected: List[int]


class Queries:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                intervals=[[1,4],[2,4],[3,6],[4,4]],
                queries=[2,3,4,5],
                expected=[3,3,1,4],
            ),
            TestCase(
                intervals=[[2,3],[2,5],[1,8],[20,25]],
                queries=[2,19,5,22],
                expected=[2,-1,4,6],
            ),
            # TestCase(intervals=???, queries=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in Queries.get_test_cases():
            actual = solver.min_interval(
                [list(iv) for iv in tc.intervals],
                list(tc.queries),
            )
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
