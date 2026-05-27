"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Op:
    kind: str                    # "update" or "sum_range"
    i: int
    j: Optional[int] = None
    val: Optional[int] = None
    expected: Optional[int] = None


@dataclass
class Problem:
    nums: List[int]
    ops: List[Op]

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(
                nums=[1, 3, 5],
                ops=[
                    Op("sum_range", 0, 2, None, 9),
                    Op("update", 1, None, 2, None),
                    Op("sum_range", 0, 2, None, 8),
                ],
            ),
            Problem(
                nums=[0, 0, 0],
                ops=[
                    Op("update", 0, None, 5, None),
                    Op("sum_range", 0, 0, None, 5),
                    Op("update", 2, None, 3, None),
                    Op("sum_range", 0, 2, None, 8),
                ],
            ),
            # Problem(nums=???, ops=[...]),  # add your own
        ]

    def run(self, solver_class) -> List[tuple]:
        """Create NumArray(list(self.nums)), replay ops; yield results for sum_range ops."""
        num_array = solver_class(list(self.nums))
        results = []
        for op in self.ops:
            if op.kind == "update":
                num_array.update(op.i, op.val)
            elif op.kind == "sum_range":
                actual = num_array.sum_range(op.i, op.j)
                passed = actual == op.expected
                results.append((op, actual, passed))
        return results

    @staticmethod
    def naive_run(problem: "Problem") -> List[tuple]:
        """Reference implementation: plain-list NumArray for correctness checking."""
        nums = list(problem.nums)
        results = []
        for op in problem.ops:
            if op.kind == "update":
                nums[op.i] = op.val
            elif op.kind == "sum_range":
                actual = sum(nums[op.i: op.j + 1])
                passed = actual == op.expected
                results.append((op, actual, passed))
        return results
