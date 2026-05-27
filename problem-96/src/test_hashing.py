"""Tests for the Hashing driver (must pass out of the box)."""

import unittest
from hashing import Hashing, _check


def _brute_longest_dup(s: str) -> str:
    """O(n²) suffix comparison — tries all lengths from largest to smallest."""
    n = len(s)
    for length in range(n - 1, 0, -1):
        seen = set()
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                return sub
            seen.add(sub)
    return ""


class TestHashing(unittest.TestCase):
    def test_expected_length_matches_brute_force(self) -> None:
        for tc in Hashing.get_test_cases():
            brute = _brute_longest_dup(tc.s)
            self.assertEqual(len(tc.expected), len(brute),
                             f"s={tc.s!r}: expected len {len(tc.expected)}, brute found len {len(brute)}")

    def test_check_helper_no_duplicate(self) -> None:
        self.assertTrue(_check("abcd", "", ""))

    def test_check_helper_wrong_length(self) -> None:
        self.assertFalse(_check("banana", "an", "ana"))

    def test_check_helper_not_in_string(self) -> None:
        self.assertFalse(_check("banana", "xyz", "ana"))


if __name__ == "__main__":
    unittest.main()
