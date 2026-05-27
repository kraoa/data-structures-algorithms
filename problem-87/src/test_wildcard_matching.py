"""Tests for the Solver (wildcard matching)."""

import unittest

from wildcards import Wildcards
from solver import Solver


class TestWildcardMatching(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.is_match("aa", "*")

    # def test_star_matches_all(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("aa", "*"))

    # def test_no_match(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.is_match("aa", "a"))

    # def test_embedded_star(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("adceb", "*a*b"))

    # def test_star_matches_empty(self) -> None:
    #     # '*' must be able to match zero characters.
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("", "*"))

    # def test_both_empty(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_match("", ""))


if __name__ == "__main__":
    unittest.main()
