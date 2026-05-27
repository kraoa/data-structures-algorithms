"""Tests for Solver."""

import unittest

from solver import Solver


class TestRotatedSearchSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.search([4, 5, 6, 7, 0, 1, 2], 0)
        # Uncomment once Solver is implemented:
        # self.assertEqual(solver.search([4,5,6,7,0,1,2], 0), 4)

    # def test_not_found(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.search([4,5,6,7,0,1,2], 3), -1)

    # def test_single_element_found(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.search([1], 1), 0)

    # def test_rotation_at_start(self) -> None:
    #     # Pivot is at index 0 (array is not actually rotated).
    #     solver = Solver()
    #     self.assertEqual(solver.search([4,5,6,7,0,1,2], 4), 0)

    # def test_two_element_array(self) -> None:
    #     # Naive "left half is sorted" logic can fail on length-2 arrays.
    #     solver = Solver()
    #     self.assertEqual(solver.search([3,1], 1), 1)


if __name__ == "__main__":
    unittest.main()
