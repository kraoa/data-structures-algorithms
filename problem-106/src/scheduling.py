"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    courses: List[List[int]]  # each [duration, lastDay]
    expected: int


class Scheduling:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[100,200],[200,1300],[1000,1250],[2000,3200]], 3),
            TestCase([[1,2]], 1),
            TestCase([[3,2],[4,3]], 0),
            TestCase([[5,5],[4,6],[2,6]], 2),
            # TestCase("???", ??),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Scheduling.get_test_cases():
            actual = solver.schedule_course([list(c) for c in tc.courses])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
