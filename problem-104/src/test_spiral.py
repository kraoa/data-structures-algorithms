"""Tests for the Spiral driver (must pass out of the box)."""

import unittest
import copy
from typing import List
from spiral import Spiral


def _brute_spiral(matrix: List[List[int]]) -> List[int]:
    """Layer-peeling reference implementation."""
    result = []
    if not matrix:
        return result
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return result


class TestSpiral(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Spiral.get_test_cases():
            brute = _brute_spiral(copy.deepcopy(tc.matrix))
            self.assertEqual(tc.expected, brute, f"matrix={tc.matrix}")

    def test_output_length_equals_total_elements(self) -> None:
        for tc in Spiral.get_test_cases():
            total = len(tc.matrix) * len(tc.matrix[0])
            self.assertEqual(len(tc.expected), total)


if __name__ == "__main__":
    unittest.main()
