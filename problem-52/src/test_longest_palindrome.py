"""Tests for Solver."""

import unittest

from solver import Solver


class TestLongestPalindromeSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.longest_palindrome("babad")
        # Uncomment once Solver is implemented:
        # result = solver.longest_palindrome("babad")
        # self.assertIn(result, ("bab", "aba"))

    # def test_even_palindrome(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.longest_palindrome("cbbd"), "bb")

    # def test_whole_string_palindrome(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.longest_palindrome("racecar"), "racecar")

    # def test_single_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.longest_palindrome("a"), "a")

    # def test_empty(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.longest_palindrome(""), "")


if __name__ == "__main__":
    unittest.main()
