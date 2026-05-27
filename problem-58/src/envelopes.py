"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    envelopes: List[List[int]]   # each envelope is [width, height]
    expected: int                # max number of envelopes that can be nested


class Problem:
    """
    You have a collection of envelopes. Envelope A fits inside envelope B only
    if both A's width and height are strictly less than B's. Find the maximum
    number of envelopes you can nest (Russian doll style).

    Example: envelopes = [[5,4],[6,4],[6,7],[2,3]] -> 3  ([2,3]->[5,4]->[6,7])
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.max_envelopes([list(e) for e in tc.envelopes])
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[5, 4], [6, 4], [6, 7], [2, 3]], 3),   # LeetCode example 1
            TestCase([[1, 1], [1, 1], [1, 1]],          1),   # LeetCode example 2; all identical
            TestCase([[1, 2]],                           1),   # single envelope
            TestCase([[1, 2], [2, 3], [3, 4], [4, 5]],  4),   # strictly increasing chain
            TestCase([[3, 3], [3, 4], [4, 4], [5, 5]],  3),   # same-width envelopes can't nest
            # TestCase([[...], [...]], ???),  # add your own
        ]
