"""Tests for Problem. Verifies stored expected values via an O(2ⁿ) brute-force."""

import unittest
from typing import List

from overlap import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(intervals: List[List[int]]) -> int:
        """Try every subset of intervals to remove; return minimum that yields non-overlapping."""
        n = len(intervals)
        best = n
        for mask in range(1 << n):
            kept = [intervals[i] for i in range(n) if not (mask >> i & 1)]
            kept.sort(key=lambda x: x[0])
            non_overlapping = True
            for j in range(1, len(kept)):
                if kept[j][0] < kept[j - 1][1]:
                    non_overlapping = False
                    break
            if non_overlapping:
                removed = bin(mask).count("1")
                best = min(best, removed)
        return best

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.intervals)
            self.assertEqual(
                tc.expected, ref,
                f"intervals={tc.intervals}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_empty(self) -> None:
        self.assertEqual(self._brute_force([]), 0)

    def test_brute_force_no_overlap(self) -> None:
        self.assertEqual(self._brute_force([[1, 2], [3, 4]]), 0)


if __name__ == "__main__":
    unittest.main()
