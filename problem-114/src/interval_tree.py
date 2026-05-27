"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str             # "insert" or "query"
    lo: int               # interval start (insert) or query point (query)
    hi: Optional[int]     # interval end (insert) or None (query)
    expected: Optional[int]  # None (insert) or count of intervals containing point (query)


class Problem:
    def __init__(self, ops: List[Op]) -> None:
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op("insert", 1, 5, None),
                Op("insert", 3, 8, None),
                Op("insert", 6, 10, None),
                Op("insert", 2, 4, None),
                Op("query", 4, None, 3),   # [1,5],[3,8],[2,4] all contain 4
                Op("query", 7, None, 2),   # [3,8],[6,10] contain 7
                Op("query", 11, None, 0),  # none contain 11
            ]),
            Problem([
                Op("insert", 0, 100, None),
                Op("query", 50, None, 1),
                Op("query", 101, None, 0),
            ]),
            # Problem([Op("???", ???, ???, None), ...]),  # add your own
        ]

    def run(self, interval_tree_class) -> List[Tuple[Op, Optional[int], bool]]:
        tree = interval_tree_class()
        results = []
        for op in self.ops:
            if op.kind == "insert":
                tree.insert(op.lo, op.hi)
                actual = None
                passed = True
            else:  # query
                actual = tree.query(op.lo)
                passed = actual == op.expected
            results.append((op, actual, passed))
        return results
