"""Tests for the Problem driver (matching.py)."""

import unittest
from matching import Problem


class TestMatching(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.text, tc.pattern),
                msg=f"text={tc.text!r} pattern={tc.pattern!r}",
            )

    def test_no_match(self) -> None:
        self.assertEqual(Problem.brute_force("abc", "xyz"), [])

    def test_overlapping_matches(self) -> None:
        self.assertEqual(Problem.brute_force("aaaa", "aa"), [0, 1, 2])

    def test_full_text_is_pattern(self) -> None:
        self.assertEqual(Problem.brute_force("abc", "abc"), [0])

    def test_pattern_longer_than_text(self) -> None:
        self.assertEqual(Problem.brute_force("ab", "abc"), [])


if __name__ == "__main__":
    unittest.main()
