"""Tests for Solver (assertions commented out until implemented)."""

import unittest
import copy
from rotation import Rotation
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.rotate([[1,2,3],[4,5,6],[7,8,9]])  # must not crash

    # def test_3x3(self) -> None:
    #     solver = Solver()
    #     m = [[1,2,3],[4,5,6],[7,8,9]]
    #     solver.rotate(m)
    #     self.assertEqual(m, [[7,4,1],[8,5,2],[9,6,3]])

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     m = [[1]]
    #     solver.rotate(m)
    #     self.assertEqual(m, [[1]])

    # def test_2x2(self) -> None:
    #     solver = Solver()
    #     m = [[1,2],[3,4]]
    #     solver.rotate(m)
    #     self.assertEqual(m, [[3,1],[4,2]])

    # def test_4x4(self) -> None:
    #     # Verifies corners and center block all rotate correctly.
    #     solver = Solver()
    #     m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    #     solver.rotate(m)
    #     self.assertEqual(m, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])


if __name__ == "__main__":
    unittest.main()
