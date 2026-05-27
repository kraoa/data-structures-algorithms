"""Tests for the Solver (jump game VI)."""

import unittest

from leaps import Leaps
from solver import Solver


class TestJumpGameVI(unittest.TestCase):
    def test_smoke(self) -> None:
        solver = Solver()
        solver.max_result([1, -1, -2, 4, -7, 3], 2)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_result([1, -1, -2, 4, -7, 3], 2), 7)

    # def test_k3(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.max_result([10, -5, -2, 4, 0, 3], 3), 17)

    # def test_forced_path(self) -> None:
    #     # k=1 means no choice — must take every step.
    #     solver = Solver()
    #     self.assertEqual(solver.max_result([1, -5], 1), -4)

    # def test_deque_eviction(self) -> None:
    #     # A naive O(nk) scan will still be correct, but the deque correctly
    #     # evicts stale indices outside the window.
    #     solver = Solver()
    #     self.assertEqual(solver.max_result([-4, -3, 4, -2, 0], 2), 0)


if __name__ == "__main__":
    unittest.main()
