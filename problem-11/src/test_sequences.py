"""Tests for Problem. Verifies stored expected values via an O(n²) DP reference."""

import unittest
from sequences import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _lis_dp(nums: list) -> int:
        """Standard O(n²) DP — correct but suboptimal reference."""
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def test_expected_values_match_dp(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._lis_dp(tc.nums)
            self.assertEqual(
                tc.expected,
                ref,
                f"nums={tc.nums}: stored={tc.expected}, dp={ref}",
            )

    def test_dp_ascending(self) -> None:
        self.assertEqual(self._lis_dp([1, 2, 3, 4, 5]), 5)

    def test_dp_descending(self) -> None:
        self.assertEqual(self._lis_dp([5, 4, 3, 2, 1]), 1)

    def test_dp_empty(self) -> None:
        self.assertEqual(self._lis_dp([]), 0)

    def test_dp_duplicates(self) -> None:
        self.assertEqual(self._lis_dp([1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
