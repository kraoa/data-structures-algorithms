"""Tests for Solver. Assertions are commented out until implemented."""

import unittest
from suffix_array import Problem
from solver import Solver


class TestSolverSuffixArray(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all test cases without asserting — stub must not crash."""
        solver = Solver()
        Problem.run(solver)

    # def test_banana(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.build("banana"), [5, 3, 1, 0, 4, 2])

    # def test_single_char(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.build("a"), [0])

    # def test_mississippi(self) -> None:
    #     # Long repeated-character string stresses the doubling logic.
    #     solver = Solver()
    #     self.assertEqual(solver.build("mississippi"), [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2])


if __name__ == "__main__":
    unittest.main()
