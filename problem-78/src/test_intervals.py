"""Tests for the Intervals driver."""

import unittest
from typing import List

from intervals import Intervals, TestCase


def _reference_merge(intervals: List[List[int]]) -> List[List[int]]:
    """O(n log n) sort-and-sweep reference implementation."""
    if not intervals:
        return []
    sorted_ivs = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_ivs[0][:]]
    for start, end in sorted_ivs[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


class TestIntervalsDriver(unittest.TestCase):
    def test_expected_values_match_reference(self) -> None:
        for tc in Intervals.get_test_cases():
            self.assertEqual(
                tc.expected,
                _reference_merge(tc.intervals),
                msg=f"Mismatch for intervals={tc.intervals}",
            )

    def test_empty_input(self) -> None:
        self.assertEqual(_reference_merge([]), [])

    def test_single_interval(self) -> None:
        self.assertEqual(_reference_merge([[5, 10]]), [[5, 10]])


if __name__ == "__main__":
    unittest.main()
