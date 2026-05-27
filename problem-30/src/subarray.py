"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: int  # maximum product of a contiguous subarray


class Problem:
    """
    Find the contiguous subarray (containing at least one number) with
    the largest product and return that product.

    Example: [2,3,-2,4] → 6  (subarray [2,3])
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.max_product(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 3, -2, 4], 6),
            TestCase([-2, 0, -1], 0),
            TestCase([-2, 3, -4], 24),
            TestCase([0, 2], 2),
            TestCase([-1], -1),
            TestCase([2, -5, -2, -4, 3], 24),  # -5 × -2 × -4 × 3 = -120; 2×-5×-2=20; -2×-4×3=24
            # TestCase([...], ?),               # add your own
        ]
