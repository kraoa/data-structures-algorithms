"""Tests for the Problem driver (connections.py)."""

import unittest
from connections import Problem


class TestConnections(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.edges),
                msg=f"edges={tc.edges}",
            )

    def test_single_redundant_triangle(self) -> None:
        self.assertEqual(Problem.brute_force([[1, 2], [1, 3], [2, 3]]), [2, 3])

    def test_last_edge_creates_cycle(self) -> None:
        result = Problem.brute_force([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
        self.assertEqual(result, [1, 4])


if __name__ == "__main__":
    unittest.main()
