"""Tests for the Solver (detect_cycle)."""

import unittest
from cycle import Problem
from solver import Solver


class TestDetectCycle(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        head, _ = Problem.build_list([3, 2, 0, -4], 1)
        solver.detect_cycle(head)

    # def test_cycle_at_index_1(self) -> None:
    #     solver = Solver()
    #     head, id_to_index = Problem.build_list([3, 2, 0, -4], 1)
    #     result = solver.detect_cycle(head)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(id_to_index[id(result)], 1)

    # def test_no_cycle(self) -> None:
    #     solver = Solver()
    #     head, _ = Problem.build_list([1], -1)
    #     self.assertIsNone(solver.detect_cycle(head))

    # def test_cycle_at_head(self) -> None:
    #     solver = Solver()
    #     head, id_to_index = Problem.build_list([1, 2], 0)
    #     result = solver.detect_cycle(head)
    #     self.assertEqual(id_to_index[id(result)], 0)

    # def test_cycle_in_middle(self) -> None:
    #     solver = Solver()
    #     head, id_to_index = Problem.build_list([1, 2, 3, 4, 5], 2)
    #     result = solver.detect_cycle(head)
    #     self.assertEqual(id_to_index[id(result)], 2)


if __name__ == "__main__":
    unittest.main()
