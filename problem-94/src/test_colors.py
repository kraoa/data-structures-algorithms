"""Tests for the Colors driver (must pass out of the box)."""

import unittest
from typing import List
from colors import Colors, TestCase


def _brute_sort(nums: List[int]) -> List[int]:
    return sorted(nums)


class TestColors(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Colors.get_test_cases():
            self.assertEqual(tc.expected, _brute_sort(tc.nums))

    def test_only_valid_colors(self) -> None:
        for tc in Colors.get_test_cases():
            for v in tc.nums:
                self.assertIn(v, (0, 1, 2))


if __name__ == "__main__":
    unittest.main()
