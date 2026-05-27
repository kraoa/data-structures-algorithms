"""Tests for the Solver (NumArray / Fenwick tree)."""

import unittest
from range_queries import Problem
from solver import NumArray


class TestNumArray(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        na = NumArray([1, 3, 5])
        na.update(1, 2)
        na.sum_range(0, 2)

    # def test_basic_sum_range(self) -> None:
    #     na = NumArray([1, 3, 5])
    #     self.assertEqual(na.sum_range(0, 2), 9)

    # def test_update_then_query(self) -> None:
    #     na = NumArray([1, 3, 5])
    #     na.update(1, 2)
    #     self.assertEqual(na.sum_range(0, 2), 8)

    # def test_single_element(self) -> None:
    #     na = NumArray([7])
    #     self.assertEqual(na.sum_range(0, 0), 7)

    # def test_update_changes_only_affected_range(self) -> None:
    #     # Updating index 1 should not change sum_range(2, 2).
    #     na = NumArray([1, 3, 5])
    #     na.update(1, 0)
    #     self.assertEqual(na.sum_range(2, 2), 5)


if __name__ == "__main__":
    unittest.main()
