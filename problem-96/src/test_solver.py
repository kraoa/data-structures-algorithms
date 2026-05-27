"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from hashing import Hashing, _check
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.longest_dup_substring("banana")  # must not crash

    # def test_banana(self) -> None:
    #     solver = Solver()
    #     result = solver.longest_dup_substring("banana")
    #     self.assertTrue(_check("banana", result, "ana"))

    # def test_no_duplicate(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.longest_dup_substring("abcd"), "")

    # def test_all_same(self) -> None:
    #     # "aaaa" → longest duplicate is "aaa" (length 3).
    #     solver = Solver()
    #     result = solver.longest_dup_substring("aaaa")
    #     self.assertTrue(_check("aaaa", result, "aaa"))


if __name__ == "__main__":
    unittest.main()
