"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    gas: List[int]
    cost: List[int]
    expected: int   # starting station index, or -1 if impossible


class Problem:
    """
    There are n gas stations arranged in a circle. Station i has gas[i] liters,
    and traveling from station i to i+1 costs cost[i] liters. Starting with an
    empty tank, find the index of the station from which you can complete the
    circuit exactly once. Return -1 if no such station exists.

    The answer is guaranteed to be unique when it exists.

    Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2] → 3
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.can_complete_circuit(gas, cost) for each test case.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.can_complete_circuit(list(tc.gas), list(tc.cost))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 2, 3, 4, 5], [3, 4, 5, 1, 2],  3),   # LeetCode example 1
            TestCase([2, 3, 4],        [3, 4, 3],        -1),   # LeetCode example 2: impossible
            TestCase([5],              [4],               0),   # single station, enough gas
            TestCase([2],              [2],               0),   # single station, exact
            TestCase([3, 1, 1],        [1, 2, 2],         0),   # start at 0
            TestCase([1, 2],           [2, 1],            1),   # must start at 1
            # TestCase([???], [???], ??),  # add your own
        ]
