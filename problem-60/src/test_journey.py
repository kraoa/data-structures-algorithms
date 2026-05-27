"""Tests for the Journey driver."""

import unittest
from typing import List

from journey import Problem


class TestJourneyDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(target: int, start_fuel: int, stations: List[List[int]]) -> int:
        """O(n^2) DP reference: dp[i] = max distance reachable with exactly i stops."""
        n = len(stations)
        dp = [start_fuel] + [0] * n
        for i, (pos, fuel) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= pos:
                    dp[t + 1] = max(dp[t + 1], dp[t] + fuel)
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.target, tc.start_fuel, tc.stations)
            self.assertEqual(tc.expected, bf,
                             f"target={tc.target} start_fuel={tc.start_fuel} stations={tc.stations}")


if __name__ == "__main__":
    unittest.main()
