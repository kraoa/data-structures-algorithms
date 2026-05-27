"""Tests for Problem. Verifies stored expected values via an O(nk) brute-force."""

import unittest
from typing import List

from window import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: List[int], k: int) -> List[int]:
        """For each window position, scan k elements to find the maximum."""
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.nums, tc.k)
            self.assertEqual(
                tc.expected, ref,
                f"nums={tc.nums}, k={tc.k}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_k_equals_length(self) -> None:
        self.assertEqual(self._brute_force([3, 1, 2], 3), [3])

    def test_brute_force_k_equals_one(self) -> None:
        self.assertEqual(self._brute_force([3, 1, 2], 1), [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
