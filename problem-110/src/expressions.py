"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    num: str
    target: int
    expected: List[str]  # sorted


class Expressions:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("123", 6, ["1*2*3", "1+2+3"]),
            TestCase("232", 8, ["2*3+2", "2+3*2"]),
            TestCase("3456237490", 9191, []),
            TestCase("105", 5, ["1*0+5", "10-5"]),
            TestCase("00", 0, ["0*0", "0+0", "0-0"]),
            # TestCase("???", ??, "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[str], bool]]:
        results = []
        for tc in Expressions.get_test_cases():
            actual = solver.add_operators(tc.num, tc.target)
            actual_sorted = sorted(actual)
            passed = actual_sorted == sorted(tc.expected)
            results.append((tc, actual_sorted, passed))
        return results
