"""Tests for the Collinear driver (must pass out of the box)."""

import unittest
from typing import List
from collinear import Collinear


def _brute_max_points(points: List[List[int]]) -> int:
    """O(n³) — for each pair (i,j) count how many other points are collinear."""
    n = len(points)
    if n == 1:
        return 1

    def collinear(p1, p2, p3) -> bool:
        # Cross product of vectors (p2-p1) and (p3-p1) equals zero.
        return ((p2[1] - p1[1]) * (p3[0] - p1[0]) ==
                (p3[1] - p1[1]) * (p2[0] - p1[0]))

    best = 2
    for i in range(n):
        for j in range(i + 1, n):
            count = 2
            for k in range(n):
                if k != i and k != j and collinear(points[i], points[j], points[k]):
                    count += 1
            best = max(best, count)
    return best


class TestCollinear(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Collinear.get_test_cases():
            brute = _brute_max_points(tc.points)
            self.assertEqual(tc.expected, brute, f"points={tc.points}")

    def test_single_point(self) -> None:
        tc = next(t for t in Collinear.get_test_cases() if len(t.points) == 1)
        self.assertEqual(tc.expected, 1)


if __name__ == "__main__":
    unittest.main()
