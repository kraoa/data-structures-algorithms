"""Read this first."""

import copy
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    left: int
    right: int
    expected: int  # minimum of nums[left..right] inclusive


class Problem:
    def __init__(self, nums: List[int], ops: List[Op]) -> None:
        self.nums = nums
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(
                [2, 4, 3, 1, 6, 7, 8, 9, 1, 7],
                [
                    Op(0, 3, 1),
                    Op(4, 7, 6),
                    Op(2, 9, 1),
                    Op(0, 0, 2),
                    Op(9, 9, 7),
                ],
            ),
            Problem([1], [Op(0, 0, 1)]),
            Problem(
                [3, 2, 1],
                [Op(0, 2, 1), Op(0, 1, 2), Op(1, 2, 1)],
            ),
            # Problem([???], [Op(???, ???, ???)]),  # add your own
        ]

    def run(self, sparse_table_class) -> List[Tuple[Op, int, bool]]:
        st = sparse_table_class(list(self.nums))
        results = []
        for op in self.ops:
            actual = st.query(op.left, op.right)
            passed = actual == op.expected
            results.append((op, actual, passed))
        return results
