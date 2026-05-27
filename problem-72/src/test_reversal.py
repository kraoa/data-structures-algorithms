"""Tests for the Problem driver (reversal.py)."""

import unittest
from reversal import Problem


class TestReversal(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.values, tc.k),
                msg=f"values={tc.values} k={tc.k}",
            )

    def test_k_equals_one_unchanged(self) -> None:
        self.assertEqual(Problem.brute_force([1, 2, 3], 1), [1, 2, 3])

    def test_partial_trailing_group_unchanged(self) -> None:
        # Last group of 2 nodes should not be reversed since k=3 > remaining.
        self.assertEqual(Problem.brute_force([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])

    def test_k_equals_length(self) -> None:
        self.assertEqual(Problem.brute_force([1, 2, 3], 3), [3, 2, 1])

    def test_build_and_to_list_roundtrip(self) -> None:
        values = [1, 2, 3, 4]
        head = Problem.build_list(values)
        self.assertEqual(Problem.to_list(head), values)


if __name__ == "__main__":
    unittest.main()
