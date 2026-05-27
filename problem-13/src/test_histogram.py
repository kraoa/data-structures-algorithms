"""Tests for Problem. Verifies stored expected values via an O(n²) brute-force."""

import unittest
from typing import List

from histogram import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(heights: List[int]) -> int:
        """O(n²) reference: try every contiguous subarray."""
        max_area = 0
        for i in range(len(heights)):
            min_h = heights[i]
            for j in range(i, len(heights)):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, min_h * (j - i + 1))
        return max_area

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.heights)
            self.assertEqual(
                tc.expected, ref,
                f"heights={tc.heights}: stored={tc.expected}, brute-force={ref}",
            )

    def test_brute_force_empty(self) -> None:
        self.assertEqual(self._brute_force([]), 0)

    def test_brute_force_uniform(self) -> None:
        self.assertEqual(self._brute_force([3, 3, 3]), 9)

    def test_brute_force_valley(self) -> None:
        self.assertEqual(self._brute_force([5, 1, 5]), 5)


if __name__ == "__main__":
    unittest.main()
