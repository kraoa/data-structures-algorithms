"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    matrix: List[List[int]]
    expected: List[int]


class Spiral:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
            TestCase([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
            TestCase([[1]], [1]),
            TestCase([[1,2],[3,4]], [1,2,4,3]),
            TestCase([[1],[2],[3]], [1,2,3]),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in Spiral.get_test_cases():
            actual = solver.spiral_order(copy.deepcopy(tc.matrix))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
