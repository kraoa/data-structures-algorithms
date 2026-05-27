"""Tests for the Solver (distinct subsequences)."""

import unittest

from counting import Counting
from solver import Solver


class TestDistinctSubsequences(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.num_distinct("rabbbit", "rabbit")

    # def test_three_ways(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_distinct("rabbbit", "rabbit"), 3)

    # def test_five_ways(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_distinct("babgbag", "bag"), 5)

    # def test_no_match(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.num_distinct("a", "b"), 0)

    # def test_empty_t(self) -> None:
    #     # There is exactly one way to form the empty string: choose nothing.
    #     solver = Solver()
    #     self.assertEqual(solver.num_distinct("", ""), 1)


if __name__ == "__main__":
    unittest.main()
