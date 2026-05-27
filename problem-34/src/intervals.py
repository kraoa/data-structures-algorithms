"""Read this first."""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class TestCase:
    intervals: List[List[int]]   # each element is [start, end]
    expected: int                # minimum number of rooms required


class Problem:
    """
    Given a list of meeting time intervals [start, end], return the minimum
    number of conference rooms required to hold all meetings simultaneously.

    Example: intervals = [[0,30],[5,10],[15,20]] → 2
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.min_meeting_rooms(intervals) for each test case.
        solver must expose .min_meeting_rooms(intervals: List[List[int]]) -> int.
        Returns (test_case, actual, passed).
        """
        import copy
        results = []
        for tc in self.test_cases:
            actual = solver.min_meeting_rooms(copy.deepcopy(tc.intervals))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[0, 30], [5, 10], [15, 20]], 2),   # LeetCode example 1
            TestCase([[7, 10], [2, 4]],             1),   # LeetCode example 2: no overlap
            TestCase([],                             0),   # no meetings
            TestCase([[1, 5], [1, 5], [1, 5]],      3),   # three simultaneous meetings
            TestCase([[0, 10], [10, 20]],            1),   # back-to-back: room reused
            TestCase([[1, 4], [2, 5], [3, 6]],       3),   # three-way overlap
            # TestCase([[???]], ??),  # add your own
        ]
