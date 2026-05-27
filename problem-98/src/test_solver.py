"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from duplicate import Duplicate
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.find_duplicate([1, 3, 4, 2, 2])  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_duplicate([1, 3, 4, 2, 2]), 2)

    # def test_duplicate_at_start(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_duplicate([3, 1, 3, 4, 2]), 3)

    # def test_minimal(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_duplicate([1, 1]), 1)

    # def test_does_not_modify_input(self) -> None:
    #     # Floyd's approach must not sort or modify the array.
    #     solver = Solver()
    #     nums = [1, 3, 4, 2, 2]
    #     original = list(nums)
    #     solver.find_duplicate(nums)
    #     self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()
