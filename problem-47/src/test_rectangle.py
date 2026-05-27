"""Tests for Problem. Verifies stored expected values via an O(n²m²) brute-force."""

import unittest
from typing import List

from rectangle import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(matrix: List[List[str]]) -> int:
        """Check every axis-aligned submatrix; track the largest all-1 rectangle."""
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(r1, m):
                    for c2 in range(c1, n):
                        if all(matrix[r][c] == "1"
                               for r in range(r1, r2 + 1)
                               for c in range(c1, c2 + 1)):
                            area = (r2 - r1 + 1) * (c2 - c1 + 1)
                            max_area = max(max_area, area)
        return max_area

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.matrix)
            self.assertEqual(
                tc.expected, ref,
                f"stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_all_zeros(self) -> None:
        self.assertEqual(self._brute_force([["0","0"],["0","0"]]), 0)

    def test_brute_force_single_one(self) -> None:
        self.assertEqual(self._brute_force([["1"]]), 1)


if __name__ == "__main__":
    unittest.main()
