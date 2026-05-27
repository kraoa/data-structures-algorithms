"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: int


class Calculator:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("1 + 1", 2),
            TestCase(" 2-1 + 2 ", 3),
            TestCase("(1+(4+5+2)-3)+(6+8)", 23),
            TestCase("2+(3-(4+5))", -4),
            TestCase("10-(2+3)", 5),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Calculator.get_test_cases():
            actual = solver.calculate(tc.s)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
