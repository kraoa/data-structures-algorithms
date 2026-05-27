"""Tests for Problem. Verifies stored expected values via a recursive minimax."""

import unittest
from typing import List

from game import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _minimax(nums: List[int]) -> bool:
        """O(2ⁿ) recursive minimax: dp(i,j) = best relative score for current player."""
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return nums[i]
            return max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))

        return dp(0, len(nums) - 1) >= 0

    def test_expected_values_match_minimax(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._minimax(tc.nums)
            self.assertEqual(
                tc.expected, ref,
                f"nums={tc.nums}: stored={tc.expected}, minimax={ref}",
            )

    def test_minimax_single_element(self) -> None:
        self.assertTrue(self._minimax([10]))

    def test_minimax_tie(self) -> None:
        self.assertTrue(self._minimax([0, 0]))


if __name__ == "__main__":
    unittest.main()
