"""Tests for the palindrome_pairs driver. Must pass out of the box."""

import unittest
from word_pairs import Problem, TestCase


def _is_palindrome(s: str) -> bool:
    return s == s[::-1]


def _brute_force(words: list) -> list:
    """O(n^2 * L) — check every ordered pair."""
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and _is_palindrome(words[i] + words[j]):
                result.append([i, j])
    return result


class TestPalindromePairsDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.words)
            self.assertEqual(
                sorted(tc.expected),
                sorted(bf),
                msg=f"words={tc.words}: stored={sorted(tc.expected)}, brute force={sorted(bf)}",
            )

    def test_run_returns_correct_structure(self) -> None:
        class _IdentitySolver:
            def palindrome_pairs(self, words):
                return []

        results = Problem.run(_IdentitySolver())
        self.assertEqual(len(results), len(Problem.get_test_cases()))
        for tc, actual, passed in results:
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, list)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
