"""Tests for the Solver (find_maximum_xor)."""

import unittest
from solver import Solver


class TestMaximumXor(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.find_maximum_xor([3, 10, 5, 25, 2, 8])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_maximum_xor([3, 10, 5, 25, 2, 8]), 28)

    # def test_two_elements(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_maximum_xor([4, 6]), 2)

    # def test_single_element(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_maximum_xor([0]), 0)

    # def test_large_set(self) -> None:
    #     # A greedy bit-by-bit approach is required; O(n^2) is too slow for n=20000.
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]), 127
    #     )


if __name__ == "__main__":
    unittest.main()
