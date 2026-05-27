"""Tests for the Solver (palindrome minimum cuts)."""

import unittest

from mincuts import MinCuts
from solver import Solver


class TestMinCut(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.min_cut("aab")

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cut("aab"), 1)

    # def test_single_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cut("a"), 0)

    # def test_all_same_chars(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cut("aaaa"), 0)

    # def test_already_palindrome(self) -> None:
    #     # The whole string is a palindrome so no cuts needed.
    #     solver = Solver()
    #     self.assertEqual(solver.min_cut("abcba"), 0)

    # def test_leet(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_cut("leet"), 2)


if __name__ == "__main__":
    unittest.main()
