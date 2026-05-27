"""Tests for the Shuffling driver (must pass out of the box)."""

import random
import unittest
from typing import List
from shuffling import Shuffling, Problem, Op


class _BruteSolution:
    """Reference implementation: list copy for reset, random.sample for shuffle."""
    def __init__(self, nums: List[int]) -> None:
        self._original = list(nums)
        self._nums = list(nums)

    def reset(self) -> List[int]:
        self._nums = list(self._original)
        return list(self._nums)

    def shuffle(self) -> List[int]:
        self._nums = random.sample(self._nums, len(self._nums))
        return list(self._nums)


class TestShuffling(unittest.TestCase):
    def test_problem_instances_are_sane(self) -> None:
        for prob in Shuffling.get_test_cases():
            self.assertGreater(len(prob.nums), 0)
            self.assertGreater(len(prob.ops), 0)

    def test_brute_solution_reset_returns_original(self) -> None:
        for prob in Shuffling.get_test_cases():
            sol = _BruteSolution(list(prob.nums))
            sol.shuffle()
            result = sol.reset()
            self.assertEqual(sorted(result), sorted(prob.nums))

    def test_brute_solution_shuffle_is_permutation(self) -> None:
        for prob in Shuffling.get_test_cases():
            sol = _BruteSolution(list(prob.nums))
            result = sol.shuffle()
            self.assertEqual(sorted(result), sorted(prob.nums))

    def test_reset_ops_have_correct_expected(self) -> None:
        for prob in Shuffling.get_test_cases():
            for op in prob.ops:
                if op.kind == "reset":
                    self.assertEqual(sorted(op.expected), sorted(prob.nums))


if __name__ == "__main__":
    unittest.main()
