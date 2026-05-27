"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    intervals: List[List[int]]   # each element is [start, end]
    expected: int                 # minimum number of intervals to remove


class Problem:
    """
    Given a list of intervals, find the minimum number of intervals to remove
    so that the remaining intervals are non-overlapping. Two intervals that
    share only an endpoint (e.g. [1,2] and [2,3]) are considered non-overlapping.

    Example: intervals = [[1,2],[2,3],[3,4],[1,3]] → 1  (remove [1,3])
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.erase_overlap_intervals(intervals) for each test case.
        solver must expose .erase_overlap_intervals(intervals: List[List[int]]) -> int.
        Returns (test_case, actual, passed).
        """
        import copy
        results = []
        for tc in self.test_cases:
            actual = solver.erase_overlap_intervals(copy.deepcopy(tc.intervals))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1,2],[2,3],[3,4],[1,3]], 1),   # LeetCode example 1
            TestCase([[1,2],[1,2],[1,2]],        2),   # LeetCode example 2
            TestCase([[1,2],[2,3]],              0),   # LeetCode example 3: no overlap
            TestCase([],                         0),   # empty
            TestCase([[1,100],[11,22],[1,11],[2,12]], 2),
            # TestCase([[???]], ??),  # add your own
        ]
