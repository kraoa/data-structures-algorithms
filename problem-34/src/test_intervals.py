"""Tests for Problem. Verifies stored expected values via a sweep-line brute-force."""

import unittest
from typing import List

from intervals import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _brute_force(intervals: List[List[int]]) -> int:
        """Sweep-line O(n²): count max concurrent meetings at any point in time."""
        if not intervals:
            return 0
        # Process end events before start events at the same time (room is freed first).
        events: List[tuple] = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort(key=lambda e: (e[0], e[1]))
        max_rooms = rooms = 0
        for _, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        return max_rooms

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.intervals)
            self.assertEqual(
                tc.expected, ref,
                f"intervals={tc.intervals}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_empty(self) -> None:
        self.assertEqual(self._brute_force([]), 0)

    def test_brute_force_back_to_back_reuses_room(self) -> None:
        self.assertEqual(self._brute_force([[0, 10], [10, 20]]), 1)


if __name__ == "__main__":
    unittest.main()
