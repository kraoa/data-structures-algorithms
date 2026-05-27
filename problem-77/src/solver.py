"""You'll implement this."""

from __future__ import annotations


class LFUCache:
    """
    Target: O(1) per get and put, O(capacity) space.
    Maintain a dict of {freq: OrderedDict{key: value}} for O(1) LRU eviction
    within each frequency bucket; track the current minimum frequency so eviction
    goes directly to the right bucket without scanning.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def get(self, key: int) -> int:
        return -1

    def put(self, key: int, value: int) -> None:
        return None
