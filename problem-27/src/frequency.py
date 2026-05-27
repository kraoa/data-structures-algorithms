"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expected: List[int]  # sorted; any valid answer has the same set of elements


class Problem:
    """
    Return the k most frequently occurring elements. The answer may be
    returned in any order; run() compares as sorted lists.

    Example: nums=[1,1,1,2,2,3], k=2 → [1,2]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        results = []
        for tc in self.test_cases:
            raw = solver.top_k_frequent(list(tc.nums), tc.k)
            actual = sorted(raw)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 1, 1, 2, 2, 3], 2, [1, 2]),
            TestCase([1], 1, [1]),
            TestCase([1, 2], 2, [1, 2]),
            TestCase([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
            TestCase([1, 1, 2, 2, 3], 2, [1, 2]),   # both 1 and 2 have freq 2; k=2 requires both
            # TestCase([...], ?, [...]),              # add your own
        ]
