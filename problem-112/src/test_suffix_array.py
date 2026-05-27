"""Tests for the suffix_array driver. Must pass out of the box."""

import unittest
from suffix_array import Problem, TestCase


def _brute_force(s: str) -> list:
    """O(n² log n) — sort indices by their suffix strings."""
    return sorted(range(len(s)), key=lambda i: s[i:])


class TestSuffixArrayDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.s)
            self.assertEqual(
                tc.expected,
                bf,
                msg=f"s={tc.s!r}: stored expected={tc.expected}, brute force={bf}",
            )

    def test_brute_force_produces_sorted_suffixes(self) -> None:
        for tc in Problem.get_test_cases():
            sa = _brute_force(tc.s)
            suffixes = [tc.s[i:] for i in sa]
            self.assertEqual(suffixes, sorted(suffixes))

    def test_run_returns_correct_structure(self) -> None:
        class BruteForceSolver:
            def build(self, s: str) -> list:
                return _brute_force(s)

        results = Problem.run(BruteForceSolver())
        tcs = Problem.get_test_cases()
        self.assertEqual(len(results), len(tcs))
        for (tc, actual, passed), orig in zip(results, tcs):
            self.assertEqual(tc, orig)
            self.assertTrue(passed)


if __name__ == "__main__":
    unittest.main()
