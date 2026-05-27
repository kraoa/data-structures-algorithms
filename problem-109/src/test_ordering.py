"""Tests for the Ordering driver (must pass out of the box)."""

import functools
import unittest
from typing import List
from ordering import Ordering


def _brute_largest_number(nums: List[int]) -> str:
    """functools.cmp_to_key with the same comparator — reference implementation."""
    def cmp(a: int, b: int) -> int:
        sa, sb = str(a), str(b)
        if sa + sb > sb + sa:
            return -1
        elif sa + sb < sb + sa:
            return 1
        return 0

    sorted_nums = sorted(nums, key=functools.cmp_to_key(cmp))
    result = "".join(str(x) for x in sorted_nums)
    return "0" if result[0] == "0" else result


class TestOrdering(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Ordering.get_test_cases():
            brute = _brute_largest_number(list(tc.nums))
            self.assertEqual(tc.expected, brute, f"nums={tc.nums}")

    def test_all_zeros_returns_zero(self) -> None:
        tc = next(t for t in Ordering.get_test_cases() if t.nums == [0, 0])
        self.assertEqual(tc.expected, "0")


if __name__ == "__main__":
    unittest.main()
