"""Tests for the Problem driver (xor.py)."""

import unittest
from xor import Problem


class TestXor(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.nums),
                msg=f"nums={tc.nums}",
            )

    def test_single_element_xor_with_itself(self) -> None:
        self.assertEqual(Problem.brute_force([0]), 0)

    def test_two_elements(self) -> None:
        self.assertEqual(Problem.brute_force([4, 6]), 2)

    def test_all_same(self) -> None:
        self.assertEqual(Problem.brute_force([7, 7, 7]), 0)


if __name__ == "__main__":
    unittest.main()
