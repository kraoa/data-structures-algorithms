"""Tests for the Problem driver (bits.py)."""

import unittest
from bits import Problem


class TestBits(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.nums),
                msg=f"nums={tc.nums}",
            )

    def test_negative_single_element(self) -> None:
        self.assertEqual(Problem.brute_force([-2, -2, 1, -2]), 1)

    def test_single_element_list(self) -> None:
        self.assertEqual(Problem.brute_force([1]), 1)

    def test_large_single_element(self) -> None:
        self.assertEqual(Problem.brute_force([0, 1, 0, 1, 0, 1, 99]), 99)


if __name__ == "__main__":
    unittest.main()
