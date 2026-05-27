"""Tests for the Inversions driver."""

import unittest
from typing import List

from inversions import Problem


class TestInversionsDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: List[int]) -> List[int]:
        """O(n^2) reference: for each element, scan right and count smaller."""
        result = []
        for i in range(len(nums)):
            count = sum(1 for j in range(i + 1, len(nums)) if nums[j] < nums[i])
            result.append(count)
        return result

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.nums)
            self.assertEqual(tc.expected, bf, f"nums={tc.nums!r}")


if __name__ == "__main__":
    unittest.main()
