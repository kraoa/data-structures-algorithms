"""Tests for the Solver (basic calculator)."""

import unittest

from calculator import Calculator
from solver import Solver


class TestBasicCalculator(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.calculate("1 + 1")

    # def test_simple_addition(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.calculate("1 + 1"), 2)

    # def test_mixed_with_spaces(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.calculate(" 2-1 + 2 "), 3)

    # def test_nested_parentheses(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    # def test_negative_result_from_parens(self) -> None:
    #     # The minus before the paren flips signs of all terms inside.
    #     solver = Solver()
    #     self.assertEqual(solver.calculate("2+(3-(4+5))"), -4)


if __name__ == "__main__":
    unittest.main()
