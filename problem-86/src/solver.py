"""You'll implement this."""

from __future__ import annotations

from typing import List

from nested import NestedInteger


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]) -> None:
        self._stack: List[NestedInteger] = []

    def next(self) -> int:
        return 0

    def hasNext(self) -> bool:
        return False
