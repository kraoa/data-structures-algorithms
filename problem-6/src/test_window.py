"""Tests for Problem. Verifies the minimum-window validator."""

import unittest
from window import Problem


class ProblemTest(unittest.TestCase):

    def _chk(self, s, t, result, expected):
        return Problem._check(s, t, result, expected)

    def test_exact_match_passes(self) -> None:
        self.assertTrue(self._chk("ADOBECODEBANC", "ABC", "BANC", "BANC"))

    def test_different_valid_window_same_length_passes(self) -> None:
        # Any valid minimum window of the correct length is acceptable.
        self.assertTrue(self._chk("aa", "a", "a", "a"))

    def test_window_too_long_fails(self) -> None:
        # "ADOBEC" is valid but not minimum.
        self.assertFalse(self._chk("ADOBECODEBANC", "ABC", "ADOBEC", "BANC"))

    def test_window_missing_char_fails(self) -> None:
        # "ADOB" is missing 'C'.
        self.assertFalse(self._chk("ADOBECODEBANC", "ABC", "ADOB", "BANC"))

    def test_no_window_exists(self) -> None:
        self.assertTrue(self._chk("a", "aa", "", ""))

    def test_nonempty_result_when_no_window_fails(self) -> None:
        self.assertFalse(self._chk("a", "aa", "a", ""))

    def test_result_not_a_substring_fails(self) -> None:
        self.assertFalse(self._chk("ab", "a", "xyz", "a"))

    def test_multiplicity_enforced(self) -> None:
        # t has two 'a's; a window with only one must fail.
        self.assertFalse(self._chk("aa", "aa", "a", "aa"))
        self.assertTrue(self._chk("aa", "aa", "aa", "aa"))


if __name__ == "__main__":
    unittest.main()
