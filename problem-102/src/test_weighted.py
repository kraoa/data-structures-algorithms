"""Tests for the Weighted driver (must pass out of the box)."""

import random
import unittest
from typing import List
from weighted import Weighted, Problem


class _BruteSolution:
    """Reference: expand weights into a flat list and use random.choice."""
    def __init__(self, w: List[int]) -> None:
        self._pool: List[int] = []
        for i, weight in enumerate(w):
            self._pool.extend([i] * weight)

    def pick_index(self) -> int:
        return random.choice(self._pool)


class TestWeighted(unittest.TestCase):
    def test_problem_instances_are_sane(self) -> None:
        for prob in Weighted.get_test_cases():
            self.assertGreater(len(prob.w), 0)
            for weight in prob.w:
                self.assertGreater(weight, 0)
            self.assertGreater(prob.trials, 0)

    def test_brute_solution_returns_valid_indices(self) -> None:
        for prob in Weighted.get_test_cases():
            sol = _BruteSolution(list(prob.w))
            for _ in range(20):
                idx = sol.pick_index()
                self.assertGreaterEqual(idx, 0)
                self.assertLess(idx, len(prob.w))


if __name__ == "__main__":
    unittest.main()
