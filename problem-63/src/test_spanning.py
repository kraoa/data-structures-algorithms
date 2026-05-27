"""Tests for the Problem driver (spanning.py)."""

import unittest
from network import Problem


class TestSpanning(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force_prim(tc.points),
                msg=f"points={tc.points}",
            )

    def test_single_point(self) -> None:
        self.assertEqual(Problem.brute_force_prim([[0, 0]]), 0)

    def test_two_points(self) -> None:
        self.assertEqual(Problem.brute_force_prim([[0, 0], [3, 4]]), 7)

    def test_unit_square(self) -> None:
        # Three edges of Manhattan distance 1 suffice for 4 corners.
        self.assertEqual(Problem.brute_force_prim([[0, 0], [1, 1], [1, 0], [0, 1]]), 3)


if __name__ == "__main__":
    unittest.main()
