"""Tests for Solver."""

import unittest

from solver import Solver


class TestInterleavingSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.is_interleave("aabcc", "dbbca", "aadbbcbcac")
        # Uncomment once Solver is implemented:
        # self.assertTrue(solver.is_interleave("aabcc", "dbbca", "aadbbcbcac"))

    # def test_false_case(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.is_interleave("aabcc", "dbbca", "aadbbbaccc"))

    # def test_both_empty(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_interleave("", "", ""))

    # def test_order_violation(self) -> None:
    #     # "abdc": uses d before c, but s2="cd" requires c first.
    #     solver = Solver()
    #     self.assertFalse(solver.is_interleave("ab", "cd", "abdc"))

    # def test_wrong_total_length(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.is_interleave("a", "b", "abc"))


if __name__ == "__main__":
    unittest.main()
