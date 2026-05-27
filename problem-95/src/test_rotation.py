"""Tests for the Rotation driver (must pass out of the box)."""

import unittest
import copy
from typing import List
from rotation import Rotation, TestCase


def _brute_rotate(matrix: List[List[int]]) -> List[List[int]]:
    """Standard 90° CW rotation using zip."""
    return [list(row) for row in zip(*matrix[::-1])]


class TestRotation(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Rotation.get_test_cases():
            self.assertEqual(tc.expected, _brute_rotate(copy.deepcopy(tc.matrix)))

    def test_output_is_square(self) -> None:
        for tc in Rotation.get_test_cases():
            n = len(tc.matrix)
            self.assertEqual(len(tc.expected), n)
            for row in tc.expected:
                self.assertEqual(len(row), n)


if __name__ == "__main__":
    unittest.main()
