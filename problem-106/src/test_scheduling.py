"""Tests for the Scheduling driver (must pass out of the box)."""

import unittest
from typing import List
from scheduling import Scheduling


def _brute_schedule(courses: List[List[int]]) -> int:
    """Backtracking — find the largest feasible subset (only for small inputs)."""
    best = [0]

    def backtrack(idx: int, time: int, count: int) -> None:
        best[0] = max(best[0], count)
        for i in range(idx, len(courses)):
            d, last = courses[i]
            if time + d <= last:
                backtrack(i + 1, time + d, count + 1)

    sorted_courses = sorted(courses, key=lambda c: c[1])
    backtrack(0, 0, 0)
    return best[0]


class TestScheduling(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Scheduling.get_test_cases():
            brute = _brute_schedule([list(c) for c in tc.courses])
            self.assertEqual(tc.expected, brute, f"courses={tc.courses}")

    def test_all_durations_positive(self) -> None:
        for tc in Scheduling.get_test_cases():
            for d, last in tc.courses:
                self.assertGreater(d, 0)
                self.assertGreater(last, 0)


if __name__ == "__main__":
    unittest.main()
