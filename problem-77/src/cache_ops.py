"""Read this first."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Op:
    kind: str               # "get" or "put"
    key: int
    value: Optional[int]    # None for get
    expected: Optional[int] # None for put


@dataclass
class Problem:
    capacity: int
    ops: List[Op]

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(
                capacity=2,
                ops=[
                    Op("put", 1, 1, None),
                    Op("put", 2, 2, None),
                    Op("get", 1, None, 1),
                    Op("put", 3, 3, None),   # evicts key 2 (freq 1, LRU among freq-1)
                    Op("get", 2, None, -1),
                    Op("get", 3, None, 3),
                    Op("put", 4, 4, None),   # evicts key 1 (freq 2 was before freq(3)=2, LRU)
                    Op("get", 1, None, -1),
                    Op("get", 3, None, 3),
                    Op("get", 4, None, 4),
                ],
            ),
            # Problem(capacity=???, ops=[...]),  # add your own
        ]

    def run(self, solver_class) -> List[tuple]:
        """Create LFUCache(capacity), replay ops; yield (op, actual, passed) for get ops."""
        lfu = solver_class(self.capacity)
        results = []
        for op in self.ops:
            if op.kind == "put":
                lfu.put(op.key, op.value)
            elif op.kind == "get":
                actual = lfu.get(op.key)
                passed = actual == op.expected
                results.append((op, actual, passed))
        return results

    @staticmethod
    def naive_run(problem: "Problem") -> List[tuple]:
        """Reference LFU using plain sorted structures for correctness checking."""
        lfu = _NaiveLFU(problem.capacity)
        results = []
        for op in problem.ops:
            if op.kind == "put":
                lfu.put(op.key, op.value)
            elif op.kind == "get":
                actual = lfu.get(op.key)
                passed = actual == op.expected
                results.append((op, actual, passed))
        return results


class _NaiveLFU:
    """Brute-force LFU: O(n) eviction via sorted scan."""

    def __init__(self, capacity: int) -> None:
        self._cap = capacity
        self._store: dict[int, int] = {}        # key -> value
        self._freq: dict[int, int] = {}         # key -> frequency
        self._order: list[int] = []             # insertion/access order (most recent last)

    def get(self, key: int) -> int:
        if key not in self._store:
            return -1
        self._freq[key] += 1
        self._order.remove(key)
        self._order.append(key)
        return self._store[key]

    def put(self, key: int, value: int) -> None:
        if self._cap == 0:
            return
        if key in self._store:
            self._store[key] = value
            self._freq[key] += 1
            self._order.remove(key)
            self._order.append(key)
            return
        if len(self._store) >= self._cap:
            # Evict the LFU key; break ties by LRU (earliest in _order).
            min_freq = min(self._freq[k] for k in self._store)
            for k in self._order:   # earliest-used first
                if self._freq[k] == min_freq:
                    del self._store[k]
                    del self._freq[k]
                    self._order.remove(k)
                    break
        self._store[key] = value
        self._freq[key] = 1
        self._order.append(key)
