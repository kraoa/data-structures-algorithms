"""Tests for the Reservoir driver (must pass out of the box)."""

import random
import unittest
from typing import Optional
from reservoir import Reservoir, Problem, ListNode, build_list


class _BruteSampler:
    """Reference sampler using random.choice on a collected list."""
    def __init__(self, head: Optional[ListNode]) -> None:
        self._values = []
        curr = head
        while curr:
            self._values.append(curr.val)
            curr = curr.next

    def get_random(self) -> int:
        return random.choice(self._values)


class TestReservoir(unittest.TestCase):
    def test_problem_instances_are_sane(self) -> None:
        for prob in Reservoir.get_test_cases():
            self.assertGreater(len(prob.values), 0)
            self.assertGreater(prob.trials, 0)

    def test_brute_sampler_returns_valid_values(self) -> None:
        for prob in Reservoir.get_test_cases():
            head = build_list(prob.values)
            sampler = _BruteSampler(head)
            value_set = set(prob.values)
            for _ in range(20):
                self.assertIn(sampler.get_random(), value_set)

    def test_build_list_single(self) -> None:
        head = build_list([42])
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 42)
        self.assertIsNone(head.next)

    def test_build_list_empty(self) -> None:
        self.assertIsNone(build_list([]))


if __name__ == "__main__":
    unittest.main()
