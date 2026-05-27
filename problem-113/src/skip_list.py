"""Read this first."""

import bisect
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str           # "insert", "search", "delete"
    val: int
    expected: Optional[bool]  # None for insert/delete; True/False for search


class Problem:
    def __init__(self, ops: List[Op]) -> None:
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op("insert", 3, None),
                Op("insert", 6, None),
                Op("insert", 7, None),
                Op("insert", 9, None),
                Op("insert", 12, None),
                Op("insert", 19, None),
                Op("search", 6, True),
                Op("search", 11, False),
                Op("delete", 6, None),
                Op("search", 6, False),
                Op("search", 9, True),
            ]),
            Problem([
                Op("insert", 1, None),
                Op("search", 1, True),
                Op("delete", 1, None),
                Op("search", 1, False),
            ]),
            # Problem([Op("???", ???, None), ...]),  # add your own
        ]

    def run(self, skip_list_class) -> List[Tuple[Op, Optional[bool], bool]]:
        sl = skip_list_class()
        results = []
        for op in self.ops:
            if op.kind == "insert":
                sl.insert(op.val)
                actual = None
                passed = True
            elif op.kind == "delete":
                sl.delete(op.val)
                actual = None
                passed = True
            else:  # search
                actual = sl.search(op.val)
                passed = actual == op.expected
            results.append((op, actual, passed))
        return results
