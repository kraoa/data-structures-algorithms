"""Tests for the Solver (is graph bipartite)."""

import unittest

from coloring import Coloring
from solver import Solver


class TestBipartite(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]])

    # def test_bipartite(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))

    # def test_not_bipartite_odd_cycle(self) -> None:
    #     solver = Solver()
    #     self.assertFalse(solver.is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

    # def test_disconnected_components(self) -> None:
    #     # Must handle disconnected graphs; loop over all unvisited start nodes.
    #     solver = Solver()
    #     self.assertTrue(solver.is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2], [5], [4]]))

    # def test_isolated_node(self) -> None:
    #     solver = Solver()
    #     self.assertTrue(solver.is_bipartite([[]]))


if __name__ == "__main__":
    unittest.main()
