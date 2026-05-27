"""Tests for Problem. Verifies stored expected values via an O(2ⁿ) brute-force."""

import unittest
from typing import List

from partitions import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: List[int]) -> bool:
        """Enumerate all 2ⁿ subsets; check if any sums to total//2."""
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        for mask in range(1 << n):
            if sum(nums[i] for i in range(n) if mask >> i & 1) == target:
                return True
        return False

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.nums)
            self.assertEqual(
                tc.expected, ref,
                f"nums={tc.nums}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_odd_sum(self) -> None:
        self.assertFalse(self._brute_force([1, 2]))

    def test_brute_force_single_element(self) -> None:
        self.assertFalse(self._brute_force([4]))


if __name__ == "__main__":
    unittest.main()
