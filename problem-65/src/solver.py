"""You'll implement this."""

from __future__ import annotations


class MyCalendarThree:
    """
    Target: O(n log n) total time, O(n) space.
    Use a difference-array style segment tree over the timeline; each book(s,e)
    increments [s,e) by 1 and the root stores the global maximum overlap count.
    Lazy propagation defers range updates; query the root for the current max k.
    """

    def __init__(self) -> None:
        pass

    def book(self, start: int, end: int) -> int:
        return 0
