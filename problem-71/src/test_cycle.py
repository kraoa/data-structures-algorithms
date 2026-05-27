"""Tests for the Problem driver (cycle.py)."""

import unittest
from cycle import Problem, ListNode


class TestCycle(unittest.TestCase):
    def _node_index(self, head, target_node, id_to_index):
        if target_node is None:
            return -1
        return id_to_index.get(id(target_node), -1)

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            head, id_to_index = Problem.build_list(tc.values, tc.cycle_pos)
            result_node = Problem.brute_force(head)
            actual = self._node_index(head, result_node, id_to_index)
            self.assertEqual(
                tc.expected,
                actual,
                msg=f"values={tc.values} cycle_pos={tc.cycle_pos}",
            )

    def test_no_cycle_returns_none(self) -> None:
        head, _ = Problem.build_list([1, 2, 3], -1)
        self.assertIsNone(Problem.brute_force(head))

    def test_single_node_no_cycle(self) -> None:
        head, _ = Problem.build_list([1], -1)
        self.assertIsNone(Problem.brute_force(head))

    def test_cycle_entry_at_head(self) -> None:
        head, id_to_index = Problem.build_list([1, 2], 0)
        result = Problem.brute_force(head)
        self.assertEqual(id_to_index[id(result)], 0)


if __name__ == "__main__":
    unittest.main()
