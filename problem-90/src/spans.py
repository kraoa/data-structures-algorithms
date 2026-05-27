"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Op:
    price: int
    expected: int


class Problem:
    def __init__(self, ops: List[Op]) -> None:
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op(100, 1),
                Op(80, 1),
                Op(60, 1),
                Op(70, 2),
                Op(60, 1),
                Op(75, 4),
                Op(85, 6),
            ]),
            Problem([
                Op(28, 1),
                Op(14, 1),
                Op(28, 3),
                Op(35, 4),
                Op(46, 5),
                Op(53, 6),
                Op(66, 7),
            ]),
            # Problem([]),  # add your own
        ]

    def run(self, spanner_class) -> List[Tuple[Op, int, bool]]:
        spanner = spanner_class()
        results = []
        for op in self.ops:
            actual = spanner.next(op.price)
            passed = actual == op.expected
            results.append((op, actual, passed))
        return results
