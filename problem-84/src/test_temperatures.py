"""Tests for the Temperatures driver."""

import unittest
from typing import List

from temperatures import Temperatures, TestCase


def _brute_force(temperatures: List[int]) -> List[int]:
    """O(n²) reference: for each day scan forward for the next warmer day."""
    n = len(temperatures)
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result


class TestTemperaturesDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Temperatures.get_test_cases():
            self.assertEqual(
                tc.expected,
                _brute_force(tc.temperatures),
                msg=f"Mismatch for temperatures={tc.temperatures}",
            )

    def test_single_element(self) -> None:
        self.assertEqual(_brute_force([42]), [0])

    def test_all_same(self) -> None:
        self.assertEqual(_brute_force([5, 5, 5]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
