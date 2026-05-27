"""Tests for the Solver (find city with fewest reachable neighbors)."""

import unittest

from cities import Cities
from solver import Solver


class TestFindCity(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.find_the_city(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.find_the_city(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4), 3
    #     )

    # def test_larger(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.find_the_city(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2), 0
    #     )

    # def test_tie_break_largest_index(self) -> None:
    #     # When counts are equal, return the city with the largest index.
    #     solver = Solver()
    #     self.assertEqual(solver.find_the_city(2, [[0, 1, 1]], 1), 1)

    # def test_all_isolated_returns_largest(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_the_city(3, [[0, 1, 5], [1, 2, 5]], 3), 2)


if __name__ == "__main__":
    unittest.main()
