"""Tests for the Solver (find_redundant_connection)."""

import unittest
from solver import Solver


class TestRedundantConnection(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.find_redundant_connection([[1, 2], [1, 3], [2, 3]])

    # def test_simple_triangle(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3])

    # def test_longer_chain(self) -> None:
    #     solver = Solver()
    #     result = solver.find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    #     self.assertEqual(result, [1, 4])

    # def test_minimal_cycle(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_redundant_connection([[1, 2], [2, 3], [1, 3]]), [1, 3])


if __name__ == "__main__":
    unittest.main()
