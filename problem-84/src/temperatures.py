"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    temperatures: List[int]
    expected: List[int]


class Temperatures:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            TestCase([30, 40, 50, 60], [1, 1, 1, 0]),
            TestCase([30, 60, 90], [1, 1, 0]),
            TestCase([90, 60, 30], [0, 0, 0]),
            TestCase([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in Temperatures.get_test_cases():
            actual = solver.daily_temperatures(list(tc.temperatures))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
