"""Tests for the Rotated driver."""

import unittest

from rotated import Problem


class TestRotatedDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: list, target: int) -> int:
        """O(n) linear scan reference."""
        try:
            return nums.index(target)
        except ValueError:
            return -1

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.nums, tc.target)
            self.assertEqual(tc.expected, bf, f"nums={tc.nums!r} target={tc.target!r}")


if __name__ == "__main__":
    unittest.main()
