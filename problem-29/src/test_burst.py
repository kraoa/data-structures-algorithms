"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from balloons import Problem
from solver import Solver


class TestBurst(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.max_coins([3, 1, 5, 8])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_coins([3, 1, 5, 8]), 167)

    # def test_single(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_coins([1]), 1)

    # def test_last_burst_choice_matters(self) -> None:
    #     # The "last balloon" in an interval contributes the most coins because
    #     # it multiplies against the sentinels on both sides of the interval.
    #     solver = Solver()
    #     self.assertEqual(solver.max_coins([1, 5]), 10)


if __name__ == "__main__":
    unittest.main()
