"""Read this first."""

import copy
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    matrix: List[List[int]]
    expected: List[List[int]]


class Rotation:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                [[1,2,3],[4,5,6],[7,8,9]],
                [[7,4,1],[8,5,2],[9,6,3]],
            ),
            TestCase(
                [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
                [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
            ),
            TestCase([[1]], [[1]]),
            TestCase([[1,2],[3,4]], [[3,1],[4,2]]),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in Rotation.get_test_cases():
            matrix_copy = copy.deepcopy(tc.matrix)
            solver.rotate(matrix_copy)
            actual = matrix_copy
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
