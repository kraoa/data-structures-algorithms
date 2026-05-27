"""Tests for Problem. Verifies stored expected values via a recursive brute-force."""

import unittest
from typing import List

from subsequences import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(text1: str, text2: str) -> int:
        """O(2^(m+n)) recursive reference — exhausts all choices."""
        m, n = len(text1), len(text2)

        def helper(i: int, j: int) -> int:
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            return max(helper(i + 1, j), helper(i, j + 1))

        return helper(0, 0)

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.text1, tc.text2)
            self.assertEqual(
                tc.expected, ref,
                f"text1={tc.text1!r}, text2={tc.text2!r}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_symmetric(self) -> None:
        self.assertEqual(self._brute_force("abc", "bca"), self._brute_force("bca", "abc"))

    def test_brute_force_empty(self) -> None:
        self.assertEqual(self._brute_force("", "anything"), 0)


if __name__ == "__main__":
    unittest.main()
