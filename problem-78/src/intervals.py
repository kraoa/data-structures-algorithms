"""Read this first."""

from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    intervals: List[List[int]]
    expected: List[List[int]]


class Intervals:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            TestCase([[1, 4], [4, 5]], [[1, 5]]),
            TestCase([[1, 4], [2, 3]], [[1, 4]]),
            TestCase([[1, 2]], [[1, 2]]),
            TestCase([[1, 4], [0, 4]], [[0, 4]]),
            TestCase([], []),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in Intervals.get_test_cases():
            actual = solver.merge(copy.deepcopy(tc.intervals))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
