"""Tests for Problem. Verifies stored expected values via a greedy formula reference."""

import unittest
from collections import Counter
from typing import List

from tasks import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _formula(tasks: List[str], n: int) -> int:
        """Closed-form greedy reference."""
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for c in counts.values() if c == max_freq)
        return max((max_freq - 1) * (n + 1) + max_count, len(tasks))

    def test_expected_values_match_formula(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._formula(tc.tasks, tc.n)
            self.assertEqual(
                tc.expected, ref,
                f"tasks={tc.tasks}, n={tc.n}: stored={tc.expected}, formula={ref}",
            )

    def test_formula_no_cooldown(self) -> None:
        self.assertEqual(self._formula(["A", "A", "A"], 0), 3)

    def test_formula_single_task(self) -> None:
        self.assertEqual(self._formula(["A"], 10), 1)


if __name__ == "__main__":
    unittest.main()
