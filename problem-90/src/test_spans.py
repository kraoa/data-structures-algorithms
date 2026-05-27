"""Tests for the Spans driver."""

import unittest
from typing import List

from spans import Op, Problem


class _NaiveSpanner:
    """Reference implementation: store all prices, scan backward on each call."""

    def __init__(self) -> None:
        self._prices: List[int] = []

    def next(self, price: int) -> int:
        self._prices.append(price)
        span = 0
        for p in reversed(self._prices):
            if p <= price:
                span += 1
            else:
                break
        return span


class TestSpansDriver(unittest.TestCase):
    def test_expected_values_match_naive(self) -> None:
        for problem in Problem.get_test_cases():
            spanner = _NaiveSpanner()
            for op in problem.ops:
                result = spanner.next(op.price)
                self.assertEqual(
                    op.expected,
                    result,
                    msg=f"Mismatch for price={op.price}",
                )

    def test_strictly_increasing_spans(self) -> None:
        spanner = _NaiveSpanner()
        prices = [1, 2, 3, 4, 5]
        for i, p in enumerate(prices):
            span = spanner.next(p)
            self.assertEqual(span, i + 1)

    def test_strictly_decreasing_all_ones(self) -> None:
        spanner = _NaiveSpanner()
        for p in [5, 4, 3, 2, 1]:
            self.assertEqual(spanner.next(p), 1)


if __name__ == "__main__":
    unittest.main()
