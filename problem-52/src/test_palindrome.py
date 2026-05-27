"""Tests for the Palindrome driver."""

import unittest

from palindrome import Problem


class TestPalindromeDriver(unittest.TestCase):

    @staticmethod
    def _brute_force(s: str) -> str:
        """O(n^3) reference: try every substring, keep the longest palindrome."""
        best = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub == sub[::-1] and len(sub) > len(best):
                    best = sub
        return best

    def test_expected_lengths_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = self._brute_force(tc.s)
            self.assertEqual(
                len(tc.expected), len(bf),
                f"s={tc.s!r}: stored expected length {len(tc.expected)} "
                f"but brute force gives {bf!r} (length {len(bf)})",
            )


if __name__ == "__main__":
    unittest.main()
