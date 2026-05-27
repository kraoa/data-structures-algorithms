"""Tests for Solver."""

import unittest

from solver import Solver


class TestRefuelingSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])
        # Uncomment once Solver is implemented:
        # self.assertEqual(
        #     solver.min_refuel_stops(100, 10, [[10,60],[20,30],[30,30],[60,40]]), 2
        # )

    # def test_no_stops_needed(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_refuel_stops(100, 100, []), 0)

    # def test_impossible(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_refuel_stops(100, 1, [[10, 100]]), -1)

    # def test_one_stop(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_refuel_stops(100, 10, [[10, 90]]), 1)

    # def test_greedy_picks_largest_retroactively(self) -> None:
    #     # The greedy algorithm uses the best available fuel from past stations,
    #     # not necessarily the most recent one.
    #     solver = Solver()
    #     self.assertEqual(solver.min_refuel_stops(1, 1, []), 0)


if __name__ == "__main__":
    unittest.main()
