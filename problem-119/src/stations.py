"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    stations: List[List[int]]
    vehicles: List[List[int]]
    expected: List[List[int]]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                stations=[[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]],
                vehicles=[[9, 2]],
                expected=[[8, 1]],
            ),
            TestCase(
                stations=[[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]],
                vehicles=[[2, 2]],
                # [1,0] (index 1) and [0,1] (index 2) are tied at dist²=5; tie broken by index → [1,0]
                expected=[[1, 0]],
            ),
            TestCase(
                stations=[[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]],
                vehicles=[[9, 4]],
                expected=[[9, 1]],
            ),
            TestCase(
                stations=[[1, 2]],
                vehicles=[[5, 5]],
                expected=[[1, 2]],
            ),
            # TestCase(stations=[???], vehicles=[???], expected=[???]),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.nearest_station(
                [list(s) for s in tc.stations],
                [list(v) for v in tc.vehicles],
            )
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
