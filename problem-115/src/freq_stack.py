"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str             # "push" or "pop"
    val: Optional[int]    # the value being pushed; None for pop
    expected: Optional[int]  # None for push; expected popped value for pop


class Problem:
    def __init__(self, ops: List[Op]) -> None:
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op("push", 5, None),
                Op("push", 7, None),
                Op("push", 5, None),
                Op("push", 7, None),
                Op("push", 4, None),
                Op("push", 5, None),
                Op("pop", None, 5),  # 5 has freq 3, highest
                Op("pop", None, 7),  # 5→freq 2, 7→freq 2 tied; 7 pushed most recently at freq=2
                Op("pop", None, 5),  # 5→freq 2 beats 7→freq 1, 4→freq 1
                Op("pop", None, 4),  # 5→freq 1, 7→freq 1, 4→freq 1 tied; 4 pushed most recently
            ]),
            Problem([
                Op("push", 1, None),
                Op("push", 1, None),
                Op("pop", None, 1),   # freq 1→2, highest; pop → 1
                Op("push", 2, None),
                Op("pop", None, 2),   # freq 1→1, 2→1 tied; 2 pushed most recently → 2
                Op("pop", None, 1),   # only 1 remains
            ]),
            # Problem([Op("???", ???, None), ...]),  # add your own
        ]

    def run(self, freq_stack_class) -> List[Tuple[Op, Optional[int], bool]]:
        fs = freq_stack_class()
        results = []
        for op in self.ops:
            if op.kind == "push":
                fs.push(op.val)
                actual = None
                passed = True
            else:  # pop
                actual = fs.pop()
                passed = actual == op.expected
            results.append((op, actual, passed))
        return results
