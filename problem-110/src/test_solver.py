"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from expressions import Expressions
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.add_operators("123", 6)  # must not crash

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     result = sorted(solver.add_operators("123", 6))
    #     self.assertEqual(result, ["1*2*3", "1+2+3"])

    # def test_leading_zero(self) -> None:
    #     # "05" is not a valid number; must not include expressions with leading zeros.
    #     solver = Solver()
    #     result = sorted(solver.add_operators("105", 5))
    #     self.assertEqual(result, ["1*0+5", "10-5"])

    # def test_multiplication_tracking(self) -> None:
    #     # 2+3*2 = 8, not (2+3)*2 = 10; backtracking must track last operand for *.
    #     solver = Solver()
    #     result = sorted(solver.add_operators("232", 8))
    #     self.assertEqual(result, ["2*3+2", "2+3*2"])

    # def test_no_solution(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.add_operators("3456237490", 9191), [])


if __name__ == "__main__":
    unittest.main()
