"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from word_pairs import Problem
from solver import Solver


class TestPalindromePairsSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     result = solver.palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    #     self.assertEqual(sorted(result), sorted([[0, 1], [1, 0], [2, 4], [3, 2]]))

    # def test_empty_string_word(self) -> None:
    #     # Empty string pairs with any palindrome word in both directions.
    #     solver = Solver()
    #     result = solver.palindrome_pairs(["a", ""])
    #     self.assertEqual(sorted(result), sorted([[0, 1], [1, 0]]))

    # def test_no_palindrome_pair(self) -> None:
    #     # "cat" + "bat" = "catbat" — not a palindrome; only symmetric pairs qualify.
    #     solver = Solver()
    #     result = solver.palindrome_pairs(["bat", "tab", "cat"])
    #     self.assertEqual(sorted(result), sorted([[0, 1], [1, 0]]))


if __name__ == "__main__":
    unittest.main()
