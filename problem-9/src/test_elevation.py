"""Tests for Problem. Verifies stored expected values via an independent brute-force."""

import unittest
from elevation import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(height: list) -> int:
        """O(n²) reference: for each bar compute its left and right maximum independently."""
        total = 0
        for i in range(len(height)):
            left_max = max(height[: i + 1])
            right_max = max(height[i:])
            total += min(left_max, right_max) - height[i]
        return total

    def test_expected_values_match_brute_force(self) -> None:
        """Every stored expected answer must agree with the brute-force calculation."""
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.height)
            self.assertEqual(
                tc.expected,
                bf,
                f"height={tc.height}: stored={tc.expected}, brute-force={bf}",
            )

    def test_brute_force_empty(self) -> None:
        self.assertEqual(self._brute_force([]), 0)

    def test_brute_force_no_valley(self) -> None:
        self.assertEqual(self._brute_force([1, 2, 3]), 0)  # ascending
        self.assertEqual(self._brute_force([3, 2, 1]), 0)  # descending

    def test_brute_force_single_valley(self) -> None:
        self.assertEqual(self._brute_force([3, 0, 3]), 3)


if __name__ == "__main__":
    unittest.main()
