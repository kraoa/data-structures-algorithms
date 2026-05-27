"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expected: int


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(nums=[7, 2, 5, 10, 8], k=2, expected=18),
            TestCase(nums=[1, 2, 3, 4, 5], k=2, expected=9),
            TestCase(nums=[1, 4, 4], k=3, expected=4),
            TestCase(nums=[2, 3, 1, 2, 4, 3], k=5, expected=4),
            TestCase(nums=[1, 2, 3, 4, 5], k=1, expected=15),
            # TestCase(nums=[???], k=???, expected=???),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in Problem.get_test_cases():
            actual = solver.split_array(list(tc.nums), tc.k)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
