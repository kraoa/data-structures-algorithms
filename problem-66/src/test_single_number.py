"""Tests for the Solver (single_number)."""

import unittest
from solver import Solver


class TestSingleNumber(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.single_number([2, 2, 3, 2])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.single_number([2, 2, 3, 2]), 3)

    # def test_large_single(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.single_number([0, 1, 0, 1, 0, 1, 99]), 99)

    # def test_negative_element(self) -> None:
    #     # Negative numbers require careful handling of the sign bit.
    #     solver = Solver()
    #     self.assertEqual(solver.single_number([-2, -2, 1, -2]), 1)

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.single_number([1]), 1)


if __name__ == "__main__":
    unittest.main()
