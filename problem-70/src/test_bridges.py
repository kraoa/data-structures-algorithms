"""Tests for the Problem driver (bridges.py)."""

import unittest
from bridges import Problem


class TestBridges(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(
                tc.expected,
                Problem.brute_force(tc.n, tc.connections),
                msg=f"n={tc.n} connections={tc.connections}",
            )

    def test_single_edge_is_bridge(self) -> None:
        self.assertEqual(Problem.brute_force(2, [[0, 1]]), [[0, 1]])

    def test_triangle_has_no_bridges(self) -> None:
        self.assertEqual(Problem.brute_force(3, [[0, 1], [1, 2], [2, 0]]), [])

    def test_chain_all_bridges(self) -> None:
        # 0-1-2 is a path; both edges are bridges.
        result = Problem.brute_force(3, [[0, 1], [1, 2]])
        self.assertEqual(result, [[0, 1], [1, 2]])


if __name__ == "__main__":
    unittest.main()
