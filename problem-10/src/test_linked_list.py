"""Tests for Problem helpers: ListNode, from_list, to_list, and test case correctness."""

import unittest
from lists import ListNode, TestCase, Problem, from_list, to_list


class ProblemTest(unittest.TestCase):

    def test_from_list_to_list_roundtrip(self) -> None:
        for values in [[], [1], [1, 2, 3], [-1, 0, 1]]:
            self.assertEqual(to_list(from_list(values)), values, f"round-trip failed for {values}")

    def test_from_list_empty_is_none(self) -> None:
        self.assertIsNone(from_list([]))

    def test_to_list_none_is_empty(self) -> None:
        self.assertEqual(to_list(None), [])

    def test_make_nodes(self) -> None:
        tc = TestCase([[1, 2], [3, 4]], [1, 2, 3, 4])
        nodes = tc.make_nodes()
        self.assertEqual(len(nodes), 2)
        self.assertEqual(to_list(nodes[0]), [1, 2])
        self.assertEqual(to_list(nodes[1]), [3, 4])

    def test_expected_is_sorted_merge_of_inputs(self) -> None:
        """Each expected answer must equal the fully sorted merge of all input lists."""
        for tc in Problem.get_test_cases():
            merged = sorted(v for lst in tc.lists for v in lst)
            self.assertEqual(
                merged,
                tc.expected,
                f"expected {tc.expected} is not the sorted merge of {tc.lists}",
            )


if __name__ == "__main__":
    unittest.main()
