"""Driver tests — all must pass out of the box."""

import unittest
from collections import Counter
from frequency import Problem, TestCase


class TestFrequency(unittest.TestCase):

    @staticmethod
    def _top_k(nums: list, k: int) -> list:
        """Reference: sort by frequency descending, take first k."""
        counts = Counter(nums)
        return sorted(sorted(counts, key=lambda x: -counts[x])[:k])

    def test_expected_values_match_reference(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._top_k(tc.nums, tc.k))

    def test_run_sorts_solver_output(self) -> None:
        """run() sorts the solver's result before comparing."""
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"top_k_frequent": lambda self, n, k: []})()
        for tc, actual, passed in problem.run(stub):
            self.assertEqual(actual, sorted(actual))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"top_k_frequent": lambda self, n, k: []})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, list)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
