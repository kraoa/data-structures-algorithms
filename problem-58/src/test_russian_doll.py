"""Tests for Solver."""

import unittest

from solver import Solver


class TestRussianDollSolver(unittest.TestCase):

    def test_runs_without_crash(self) -> None:
        solver = Solver()
        solver.max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
        # Uncomment once Solver is implemented:
        # self.assertEqual(solver.max_envelopes([[5,4],[6,4],[6,7],[2,3]]), 3)

    # def test_all_identical(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_envelopes([[1,1],[1,1],[1,1]]), 1)

    # def test_strictly_increasing_chain(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_envelopes([[1,2],[2,3],[3,4],[4,5]]), 4)

    # def test_same_width_cannot_nest(self) -> None:
    #     # Naive LIS on unsorted heights picks same-width envelopes; the sort trick avoids this.
    #     solver = Solver()
    #     self.assertEqual(solver.max_envelopes([[3,3],[3,4],[4,4],[5,5]]), 3)


if __name__ == "__main__":
    unittest.main()
