"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from window import Problem
from solver import Solver


class TestAnagrams(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.find_anagrams("cbaebabacd", "abc")

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(sorted(solver.find_anagrams("cbaebabacd", "abc")), [0, 6])

    # def test_consecutive_anagrams(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(sorted(solver.find_anagrams("abab", "ab")), [0, 1, 2])

    # def test_no_match(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_anagrams("aa", "bb"), [])


if __name__ == "__main__":
    unittest.main()
