"""Tests for Problem. Verifies stored expected values via an O(n²) brute-force."""

import unittest
from typing import List

from stations import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(gas: List[int], cost: List[int]) -> int:
        """Try each station as start; simulate the full circuit."""
        n = len(gas)
        for start in range(n):
            tank = 0
            ok = True
            for step in range(n):
                i = (start + step) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    ok = False
                    break
            if ok:
                return start
        return -1

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.gas, tc.cost)
            self.assertEqual(
                tc.expected, ref,
                f"gas={tc.gas}, cost={tc.cost}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_impossible(self) -> None:
        self.assertEqual(self._brute_force([1], [2]), -1)

    def test_brute_force_uniqueness(self) -> None:
        # When a solution exists, there is exactly one valid starting index.
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        start = self._brute_force(gas, cost)
        self.assertNotEqual(start, -1)
        n = len(gas)
        for s in range(n):
            if s != start:
                tank = 0
                ok = True
                for step in range(n):
                    tank += gas[(s + step) % n] - cost[(s + step) % n]
                    if tank < 0:
                        ok = False
                        break
                self.assertFalse(ok, f"found second valid start at {s}")


if __name__ == "__main__":
    unittest.main()
