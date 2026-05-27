"""Tests for Problem. Verifies stored expected values using Python's re module."""

import re
import unittest
from patterns import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _re_match(s: str, p: str) -> bool:
        """Use Python's regex engine as a reference for this subset of patterns."""
        return re.fullmatch(p, s) is not None

    def test_expected_values_match_re(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._re_match(tc.s, tc.p)
            self.assertEqual(
                tc.expected, ref,
                f"s={repr(tc.s)}, p={repr(tc.p)}: stored={tc.expected}, re={ref}",
            )

    def test_re_dot_wildcard(self) -> None:
        self.assertTrue(self._re_match("a", "."))
        self.assertFalse(self._re_match("ab", "."))

    def test_re_star_zero_occurrences(self) -> None:
        self.assertTrue(self._re_match("b", "a*b"))

    def test_re_star_many_occurrences(self) -> None:
        self.assertTrue(self._re_match("aaab", "a*b"))

    def test_re_empty(self) -> None:
        self.assertTrue(self._re_match("", ""))
        self.assertTrue(self._re_match("", "a*"))
        self.assertFalse(self._re_match("", "a"))


if __name__ == "__main__":
    unittest.main()
