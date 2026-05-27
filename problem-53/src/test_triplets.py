"""Tests for the Triplets driver."""

import unittest
from itertools import combinations
from typing import List

from triplets import Problem


class TestTripletsDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: List[int]) -> List[List[int]]:
        """O(n^3) reference: check every combination of three elements."""
        found = set()
        for a, b, c in combinations(nums, 3):
            if a + b + c == 0:
                found.add(tuple(sorted([a, b, c])))
        return sorted(list(t) for t in found)

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.nums)
            normalized = sorted(sorted(t) for t in tc.expected)
            self.assertEqual(normalized, bf, f"nums={tc.nums!r}")


if __name__ == "__main__":
    unittest.main()
