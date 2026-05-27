"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    candidates: List[int]   # distinct positive integers
    target: int
    expected: List[List[int]]  # each combination sorted; outer list sorted


class Problem:
    """
    Find all unique combinations of candidates that sum to target.
    The same number may be used an unlimited number of times.
    Combinations are returned in sorted order (no duplicates).

    Example: candidates=[2,3,6,7], target=7 → [[2,2,3],[7]]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, object, bool]]:
        results = []
        for tc in self.test_cases:
            raw = solver.combination_sum(list(tc.candidates), tc.target)
            actual = sorted(sorted(c) for c in raw)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            TestCase([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            TestCase([2], 1, []),                   # impossible
            TestCase([1], 1, [[1]]),                # single step
            TestCase([1], 3, [[1, 1, 1]]),          # repeated use
            # TestCase([...], ?, [...]),             # add your own
        ]
