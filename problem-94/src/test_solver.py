"""Tests for Solver (assertions commented out until implemented)."""

import unittest
from colors import Colors
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        nums = [2, 0, 2, 1, 1, 0]
        solver.sort_colors(nums)  # must not crash

    # def test_basic_case(self) -> None:
    #     solver = Solver()
    #     nums = [2, 0, 2, 1, 1, 0]
    #     solver.sort_colors(nums)
    #     self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     nums = [0]
    #     solver.sort_colors(nums)
    #     self.assertEqual(nums, [0])

    # def test_all_same(self) -> None:
    #     # All 2s — must not move anything incorrectly.
    #     solver = Solver()
    #     nums = [2, 2, 2]
    #     solver.sort_colors(nums)
    #     self.assertEqual(nums, [2, 2, 2])

    # def test_already_sorted(self) -> None:
    #     solver = Solver()
    #     nums = [0, 1, 2]
    #     solver.sort_colors(nums)
    #     self.assertEqual(nums, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
