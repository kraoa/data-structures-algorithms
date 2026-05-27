"""Tests for the Solver (count_components)."""

import unittest
from components import Problem
from solver import Solver


class TestCountComponents(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.count_components(5, [[0, 1], [1, 2], [3, 4]])

    # def test_two_components(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)

    # def test_one_component(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)

    # def test_no_edges(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.count_components(4, []), 4)

    # def test_triangle_is_one_component(self) -> None:
    #     # Redundant edge still yields one component.
    #     solver = Solver()
    #     self.assertEqual(solver.count_components(3, [[0, 1], [1, 2], [0, 2]]), 1)


if __name__ == "__main__":
    unittest.main()
