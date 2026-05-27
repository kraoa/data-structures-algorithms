"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from jumps import Problem
from solver import Solver


class TestJumpGame(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.min_jumps([2, 3, 1, 1, 4])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_jumps([2, 3, 1, 1, 4]), 2)

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_jumps([1]), 0)

    # def test_greedy_must_look_across_whole_window(self) -> None:
    #     # Naive greedy (always jump as far as possible immediately) gets 3.
    #     # Correct greedy scans the window and picks the best launch point.
    #     solver = Solver()
    #     self.assertEqual(solver.min_jumps([1, 2, 3, 4, 5]), 3)


if __name__ == "__main__":
    unittest.main()
