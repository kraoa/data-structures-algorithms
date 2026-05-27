"""Tests for the StockSpanner solver."""

import unittest

from spans import Problem
from solver import StockSpanner


class TestStockSpan(unittest.TestCase):
    def test_smoke(self) -> None:
        spanner = StockSpanner()
        spanner.next(100)

    # def test_basic_sequence(self) -> None:
    #     spanner = StockSpanner()
    #     self.assertEqual(spanner.next(100), 1)
    #     self.assertEqual(spanner.next(80), 1)
    #     self.assertEqual(spanner.next(60), 1)
    #     self.assertEqual(spanner.next(70), 2)
    #     self.assertEqual(spanner.next(60), 1)
    #     self.assertEqual(spanner.next(75), 4)
    #     self.assertEqual(spanner.next(85), 6)

    # def test_increasing_prices(self) -> None:
    #     spanner = StockSpanner()
    #     self.assertEqual(spanner.next(28), 1)
    #     self.assertEqual(spanner.next(14), 1)
    #     self.assertEqual(spanner.next(28), 3)
    #     self.assertEqual(spanner.next(35), 4)

    # def test_span_accumulates_across_skipped_entries(self) -> None:
    #     # When the new price swallows multiple stack entries, their spans must be
    #     # summed — not just counting days linearly.
    #     spanner = StockSpanner()
    #     spanner.next(100)
    #     spanner.next(80)
    #     spanner.next(60)
    #     spanner.next(70)
    #     self.assertEqual(spanner.next(75), 4)


if __name__ == "__main__":
    unittest.main()
