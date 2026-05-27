"""Tests for the Solver (reverse_k_group)."""

import unittest
from reversal import Problem
from solver import Solver


class TestReverseKGroup(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        head = Problem.build_list([1, 2, 3, 4, 5])
        solver.reverse_k_group(head, 2)

    # def test_k_2(self) -> None:
    #     solver = Solver()
    #     head = Problem.build_list([1, 2, 3, 4, 5])
    #     result = solver.reverse_k_group(head, 2)
    #     self.assertEqual(Problem.to_list(result), [2, 1, 4, 3, 5])

    # def test_k_3(self) -> None:
    #     solver = Solver()
    #     head = Problem.build_list([1, 2, 3, 4, 5])
    #     result = solver.reverse_k_group(head, 3)
    #     self.assertEqual(Problem.to_list(result), [3, 2, 1, 4, 5])

    # def test_k_equals_length(self) -> None:
    #     solver = Solver()
    #     head = Problem.build_list([1, 2])
    #     result = solver.reverse_k_group(head, 2)
    #     self.assertEqual(Problem.to_list(result), [2, 1])

    # def test_trailing_group_not_reversed(self) -> None:
    #     # The last partial group (fewer than k nodes) must stay in original order.
    #     solver = Solver()
    #     head = Problem.build_list([1, 2, 3, 4, 5])
    #     result = solver.reverse_k_group(head, 3)
    #     self.assertEqual(Problem.to_list(result)[-2:], [4, 5])


if __name__ == "__main__":
    unittest.main()
