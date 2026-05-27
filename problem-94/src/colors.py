"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: List[int]


class Colors:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            TestCase([2, 0, 1], [0, 1, 2]),
            TestCase([0], [0]),
            TestCase([1], [1]),
            TestCase([0, 0, 0], [0, 0, 0]),
            TestCase([2, 2, 2], [2, 2, 2]),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in Colors.get_test_cases():
            nums_copy = list(tc.nums)
            solver.sort_colors(nums_copy)
            actual = nums_copy
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
