"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    """A single cache operation."""

    kind: str           # "get" or "put"
    key: int
    value: Optional[int]    # only used for "put"
    expected: Optional[int] # expected return value for "get"; None for "put"

    def __repr__(self) -> str:
        if self.kind == "put":
            return f"put({self.key}, {self.value})"
        return f"get({self.key}) -> {self.expected}"


class Problem:
    """
    Defines a sequence of cache operations with expected outputs.

    Call run() with your LRUCache instance to replay the operations and
    get back a list of (op, actual_value, passed) for every get.
    """

    def __init__(self, capacity: int, ops: List[Op]):
        self.capacity = capacity
        self.ops = ops

    def run(self, cache) -> List[Tuple[Op, int, bool]]:
        """
        Replays all ops against cache.
        cache must expose .get(key: int) -> int
                      and .put(key: int, value: int) -> None.
        Returns (op, actual, passed) tuples for every get operation.
        """
        results = []
        for op in self.ops:
            if op.kind == "put":
                cache.put(op.key, op.value)
            else:
                actual = cache.get(op.key)
                results.append((op, actual, actual == op.expected))
        return results

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            # LeetCode example
            Problem(2, [
                Op("put", 1, 1,  None),
                Op("put", 2, 2,  None),
                Op("get", 1, None, 1),    # {1=1, 2=2}
                Op("put", 3, 3,  None),   # evicts 2   → {1=1, 3=3}
                Op("get", 2, None, -1),   # evicted
                Op("put", 4, 4,  None),   # evicts 1   → {3=3, 4=4}
                Op("get", 1, None, -1),   # evicted
                Op("get", 3, None,  3),
                Op("get", 4, None,  4),
            ]),
            # capacity 1
            Problem(1, [
                Op("put", 2, 1,  None),
                Op("get", 2, None,  1),
                Op("put", 3, 2,  None),   # evicts 2
                Op("get", 2, None, -1),   # evicted
                Op("get", 3, None,  2),
            ]),
            # get promotes recency — evicts the right key
            Problem(2, [
                Op("put", 1, 10, None),
                Op("put", 2, 20, None),
                Op("get", 1, None, 10),   # 1 is now most-recent; 2 is LRU
                Op("put", 3, 30, None),   # evicts 2, not 1
                Op("get", 2, None, -1),   # evicted
                Op("get", 1, None, 10),
                Op("get", 3, None, 30),
            ]),
        ]
