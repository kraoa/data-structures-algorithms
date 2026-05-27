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
                Op("insert", 30, None),
                Op("inorder", None, [10, 20, 30]),
                Op("insert", 15, None),
                Op("insert", 25, None),
                Op("inorder", None, [10, 15, 20, 25, 30]),
                Op("search", 20, True),
                Op("search", 17, False),
            ]),
            Problem([
                Op("insert", 7, None),
                Op("insert", 3, None),
                Op("insert", 18, None),
                Op("insert", 10, None),
                Op("insert", 22, None),
                Op("insert", 8, None),
                Op("insert", 26, None),
                Op("inorder", None, [3, 7, 8, 10, 18, 22, 26]),
            ]),
            # Problem([Op("???", ???, None), ...]),  # add your own
        ]

    def run(self, rb_tree_class) -> List[Tuple[Op, Any, bool]]:
        tree = rb_tree_class()
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
