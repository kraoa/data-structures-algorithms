"""Tests for the multiplication driver. Must pass out of the box."""

import unittest

from multiplication import Problem, TestCase


def _brute_force(m: int, n: int, k: int) -> int:
    """Generate all m*n table values, sort, return the k-th (1-indexed)."""
    values = sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))
    return values[k - 1]


class TestMultiplicationDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.m, tc.n, tc.k)
            self.assertEqual(
                tc.expected,
                bf,
                msg=f"m={tc.m}, n={tc.n}, k={tc.k}: stored={tc.expected}, brute force={bf}",
            )

    def test_run_returns_correct_structure(self) -> None:
        class _ZeroSolver:
            def find_kth_number(self, m, n, k):
                return 0

        results = Problem.run(_ZeroSolver())
        self.assertEqual(len(results), len(Problem.get_test_cases()))
        for tc, actual, passed in results:
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
