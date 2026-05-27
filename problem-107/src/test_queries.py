"""Tests for the Queries driver (must pass out of the box)."""

import unittest
from typing import List
from queries import Queries


def _brute_min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """O(n*q) — for each query scan all intervals and find the smallest containing one."""
    result = []
    for q in queries:
        best = -1
        for start, end in intervals:
            if start <= q <= end:
                size = end - start + 1
                if best == -1 or size < best:
                    best = size
        result.append(best)
    return result


class TestQueries(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Queries.get_test_cases():
            brute = _brute_min_interval(
                [list(iv) for iv in tc.intervals],
                list(tc.queries),
            )
            self.assertEqual(tc.expected, brute,
                             f"intervals={tc.intervals} queries={tc.queries}")

    def test_output_length_matches_query_count(self) -> None:
        for tc in Queries.get_test_cases():
            self.assertEqual(len(tc.expected), len(tc.queries))


if __name__ == "__main__":
    unittest.main()
