"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from printer import Printer
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.strange_printer("aaabbb")  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.strange_printer("aaabbb"), 2)

    # def test_aba(self) -> None:
    #     # Greedy (one char at a time) gives 3; correct DP gives 2.
    #     solver = Solver()
    #     self.assertEqual(solver.strange_printer("aba"), 2)

    # def test_single_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.strange_printer("a"), 1)

    # def test_repeated_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.strange_printer("aa"), 1)


if __name__ == "__main__":
    unittest.main()
