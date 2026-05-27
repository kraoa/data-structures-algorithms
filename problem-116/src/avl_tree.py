"""Read this first."""

from dataclasses import dataclass
from typing import Any, List, Optional, Tuple


@dataclass
class Op:
    kind: str                # "insert", "search", "inorder"
    val: Optional[int]       # for insert/search; None for inorder
    expected: Optional[Any]  # None (insert); bool (search); List[int] (inorder)


class Problem:
    def __init__(self, ops: List[Op]) -> None:
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op("insert", 10, None),
                Op("insert", 20, None),
                Op("insert", 30, None),   # triggers left rotation
                Op("inorder", None, [10, 20, 30]),
                Op("insert", 40, None),
                Op("insert", 50, None),   # more rotations
                Op("inorder", None, [10, 20, 30, 40, 50]),
                Op("search", 30, True),
                Op("search", 25, False),
            ]),
            Problem([
                Op("insert", 5, None),
                Op("insert", 3, None),
                Op("insert", 1, None),   # triggers right rotation
                Op("inorder", None, [1, 3, 5]),
                Op("insert", 4, None),   # triggers LR rotation
                Op("inorder", None, [1, 3, 4, 5]),
            ]),
            # Problem([Op("???", ???, None), ...]),  # add your own
        ]

    def run(self, avl_tree_class) -> List[Tuple[Op, Any, bool]]:
        tree = avl_tree_class()
        results = []
        for op in self.ops:
            if op.kind == "insert":
                tree.insert(op.val)
                actual = None
                passed = True
            elif op.kind == "search":
                actual = tree.search(op.val)
                passed = actual == op.expected
            else:  # inorder
                actual = tree.inorder()
                passed = actual == op.expected
            results.append((op, actual, passed))
        return results
