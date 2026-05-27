"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    target: int
    start_fuel: int
    stations: List[List[int]]  # each station is [position, fuel_available]
    expected: int               # min stops to reach target, or -1 if impossible


class Problem:
    """
    A car starts at position 0 with start_fuel litres of fuel. It travels 1 unit
    per litre. Stations are at given positions with given fuel amounts available.
    Return the minimum number of refuelling stops needed to reach target, or -1
    if it is not possible.

    Example: target=100, start_fuel=10, stations=[[10,60],[20,30],[30,30],[60,40]] -> 2
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.min_refuel_stops(
                tc.target, tc.start_fuel, [list(s) for s in tc.stations]
            )
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(1,   1,  [],                                    0),  # LeetCode example 1
            TestCase(100, 1,  [[10, 100]],                          -1),  # LeetCode example 2
            TestCase(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),  # LeetCode example 3
            TestCase(100, 100, [],                                   0),  # enough fuel to start
            TestCase(100, 10, [[10, 90]],                            1),  # one stop suffices
            TestCase(100, 5,  [[4, 4], [8, 4], [12, 4]],             -1),  # stations too sparse
            # TestCase(???, ???, [...], ???),  # add your own
        ]
