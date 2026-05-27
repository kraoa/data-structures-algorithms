"""Tests for the RangeCount driver (must pass out of the box)."""

import unittest
from typing import List
from range_count import RangeCount


def _brute_count_range_sum(nums: List[int], lower: int, upper: int) -> int:
    """O(n²) — compute all contiguous range sums and count those in [lower, upper]."""
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if lower <= total <= upper:
                count += 1
    return count


class TestRangeCount(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in RangeCount.get_test_cases():
            brute = _brute_count_range_sum(tc.nums, tc.lower, tc.upper)
            self.assertEqual(tc.expected, brute,
                             f"nums={tc.nums} lower={tc.lower} upper={tc.upper}")

    def test_lower_le_upper(self) -> None:
        for tc in RangeCount.get_test_cases():
            self.assertLessEqual(tc.lower, tc.upper)


if __name__ == "__main__":
    unittest.main()
