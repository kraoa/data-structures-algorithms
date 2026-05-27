"""You'll implement this."""


class LRUCache:
    """
    Least Recently Used cache.

    get(key)        — return the cached value, or -1 if not present.
                      Marks key as the most recently used.
    put(key, value) — insert or update the value.
                      If adding a new key would exceed capacity, first evict
                      the least recently used key.

    Both operations must run in O(1) average time.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        return -1

    def put(self, key: int, value: int) -> None:
        pass
