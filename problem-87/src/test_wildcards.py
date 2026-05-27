"""Tests for the Wildcards driver."""

import re
import unittest

from wildcards import Wildcards, TestCase


def _regex_reference(s: str, p: str) -> bool:
    """Convert wildcard pattern to regex: '?' -> '.', '*' -> '.*'."""
    regex = re.sub(r'\*', '.*', re.sub(r'\?', '.', p))
    return re.fullmatch(regex, s) is not None


class TestWildcardsDriver(unittest.TestCase):
    def test_expected_values_match_regex(self) -> None:
        for tc in Wildcards.get_test_cases():
            result = _regex_reference(tc.s, tc.p)
            self.assertEqual(
                tc.expected,
                result,
                msg=f"Mismatch for s={tc.s!r}, p={tc.p!r}",
            )

    def test_question_mark_matches_exactly_one(self) -> None:
        self.assertTrue(_regex_reference("a", "?"))
        self.assertFalse(_regex_reference("", "?"))
        self.assertFalse(_regex_reference("ab", "?"))

    def test_star_matches_empty(self) -> None:
        self.assertTrue(_regex_reference("", "*"))


if __name__ == "__main__":
    unittest.main()
