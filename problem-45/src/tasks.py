"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    tasks: List[str]  # each character is a task type
    n: int            # cooldown: same task type must be at least n intervals apart
    expected: int     # minimum number of CPU intervals (including idles)


class Problem:
    """
    Given a list of tasks (identified by uppercase letters) and a cooldown n,
    find the minimum number of CPU intervals to finish all tasks. The CPU may
    be idle when no eligible task is available.

    Example: tasks=["A","A","A","B","B","B"], n=2 → 8
             (A → B → idle → A → B → idle → A → B)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.least_interval(tasks, n) for each test case.
        solver must expose .least_interval(tasks: List[str], n: int) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.least_interval(list(tc.tasks), tc.n)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(["A","A","A","B","B","B"],              2, 8),   # LeetCode example 1
            TestCase(["A","C","A","B","D","B"],              1, 6),   # LeetCode example 2
            TestCase(["A","A","A","B","B","B"],              0, 6),   # LeetCode example 3: no cooldown
            TestCase(["A"],                                  2, 1),   # single task
            TestCase(["A","A","A","A","A","A",
                      "B","C","D","E","F","G"],              2, 16),  # idle slots needed
            # TestCase([???], ??, ??),  # add your own
        ]
