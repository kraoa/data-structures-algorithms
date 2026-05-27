"""Tests for the Solver (daily temperatures)."""

import unittest

from temperatures import Temperatures
from solver import Solver


class TestDailyTemperatures(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
    #         [1, 1, 4, 2, 1, 1, 0, 0],
    #     )

    # def test_strictly_increasing(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    # def test_strictly_decreasing(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.daily_temperatures([90, 60, 30]), [0, 0, 0])

    # def test_long_wait(self) -> None:
    #     # Index 0 (89) must wait all the way to index 8 (100).
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.daily_temperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]),
    #         [8, 1, 5, 4, 3, 2, 1, 1, 0, 0],
    #     )


if __name__ == "__main__":
    unittest.main()
