"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    heights: List[int]
    expected: int  # area of the largest rectangle


class Problem:
    """
    Given an array of bar heights in a histogram (each bar has width 1),
    return the area of the largest rectangle that can be formed.

    Example: [2, 1, 5, 6, 2, 3] → 10  (bars at index 2–3, height 5, width 2)

    O(n²) brute force works. Aim for O(n) using a monotonic stack.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.largest_rectangle(heights) for each test case.
        solver must expose .largest_rectangle(heights: List[int]) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.largest_rectangle(list(tc.heights))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([2, 1, 5, 6, 2, 3], 10),  # LeetCode example 1
            TestCase([2, 4],              4),   # LeetCode example 2
            TestCase([1],                 1),
            TestCase([0],                 0),
            TestCase([],                  0),
            TestCase([1, 2, 3, 4, 5],    9),   # ascending: 3×3
            TestCase([5, 4, 3, 2, 1],    9),   # descending: 3×3
            TestCase([6, 2, 5, 4, 5, 1, 6], 12),
            # TestCase([...], ?),  # add your own
        ]
