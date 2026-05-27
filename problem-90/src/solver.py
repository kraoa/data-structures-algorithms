"""You'll implement this."""

from __future__ import annotations


class StockSpanner:
    def __init__(self) -> None:
        self._stack: list = []  # list of (price, span)

    def next(self, price: int) -> int:
        return 0
