"""Tests for the splits driver. Must pass out of the box."""

import unittest
from typing import List

from splits import Problem, TestCase


def _brute_force(nums: List[int], k: int) -> int:
    """O(n^2 * k) DP — dp[i][j] = min largest-sum splitting nums[:j] into i parts."""
    n = len(nums)
    INF = float("inf")
    # prefix[j] = sum(nums[:j])
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # dp[i][j]: min of max-subarray-sum when splitting nums[:j] into i subarrays
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    for parts in range(1, k + 1):
        for j in range(parts, n + 1):
            for m in range(parts - 1, j):
                segment = prefix[j] - prefix[m]
                dp[parts][j] = min(dp[parts][j], max(dp[parts - 1][m], segment))
    return dp[k][n]


class TestSplitsDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.nums, tc.k)
            self.assertEqual(
                tc.expected,
                bf,
                msg=f"nums={tc.nums}, k={tc.k}: stored={tc.expected}, brute force={bf}",
            )

    def test_run_returns_correct_structure(self) -> None:
        class _ZeroSolver:
            def split_array(self, nums, k):
                return 0

        results = Problem.run(_ZeroSolver())
        self.assertEqual(len(results), len(Problem.get_test_cases()))
        for tc, actual, passed in results:
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
