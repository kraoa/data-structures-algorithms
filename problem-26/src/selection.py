"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expected: int  # kth largest value (not kth largest distinct)


class Problem:
    """
    Return the kth largest element in the array (1-indexed, so k=1 is
    the maximum). Elements are not necessarily distinct.

    Example: nums=[3,2,1,5,6,4], k=2 → 5
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.find_kth_largest(list(tc.nums), tc.k)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([3, 2, 1, 5, 6, 4], 2, 5),
            TestCase([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            TestCase([1], 1, 1),
            TestCase([1, 2], 2, 1),
            TestCase([7, 6, 5, 4, 3, 2, 1], 5, 3),
            # TestCase([...], ?, ?),  # add your own
        ]
