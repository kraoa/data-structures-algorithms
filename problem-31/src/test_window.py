"""Driver tests — all must pass out of the box."""

import unittest
from collections import Counter
from window import Problem, TestCase


class TestWindow(unittest.TestCase):

    @staticmethod
    def _naive(s: str, p: str) -> list:
        """O(n × |p|): check every window of length |p|."""
        target = Counter(p)
        k = len(p)
        return sorted(i for i in range(len(s) - k + 1) if Counter(s[i:i + k]) == target)

    def test_expected_values_match_naive(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._naive(tc.s, tc.p))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"find_anagrams": lambda self, s, p: []})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, list)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
