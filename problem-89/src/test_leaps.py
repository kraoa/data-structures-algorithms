"""Tests for the Leaps driver."""

import unittest
from typing import List

from leaps import Leaps, TestCase


def _brute_force(nums: List[int], k: int) -> int:
    """O(nk) DP reference: for each index scan back up to k steps."""
    n = len(nums)
    dp = [float("-inf")] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + max(dp[max(0, i - k): i])
    return int(dp[n - 1])


class TestLeapsDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Leaps.get_test_cases():
            result = _brute_force(tc.nums, tc.k)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for nums={tc.nums}, k={tc.k}",
            )

    def test_single_element(self) -> None:
        self.assertEqual(_brute_force([1], 1), 1)

    def test_k_equals_length(self) -> None:
        self.assertEqual(_brute_force([1, 2, 3], 3), 6)


if __name__ == "__main__":
    unittest.main()
