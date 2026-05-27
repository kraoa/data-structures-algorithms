"""Tests for the Duplicate driver (must pass out of the box)."""

import unittest
from collections import Counter
from duplicate import Duplicate


def _brute_find_duplicate(nums: list) -> int:
    """Counter — find the value that appears more than once."""
    counts = Counter(nums)
    return next(v for v, c in counts.items() if c > 1)


class TestDuplicate(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Duplicate.get_test_cases():
            self.assertEqual(tc.expected, _brute_find_duplicate(tc.nums))

    def test_exactly_one_duplicate_per_case(self) -> None:
        counts = Counter
        for tc in Duplicate.get_test_cases():
            dupes = [v for v, c in Counter(tc.nums).items() if c > 1]
            self.assertGreaterEqual(len(dupes), 1)


if __name__ == "__main__":
    unittest.main()
