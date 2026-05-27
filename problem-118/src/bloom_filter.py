"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str              # "add" or "might_contain"
    item: str
    # None for add; True if item was added (no false negatives);
    # None if item was NOT added (false positive possible — skip assertion)
    expected: Optional[bool]


class Problem:
    def __init__(self, size: int, num_hashes: int, ops: List[Op]) -> None:
        self.size = size
        self.num_hashes = num_hashes
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(1000, 3, [
                Op("add", "hello", None),
                Op("add", "world", None),
                Op("add", "foo", None),
                Op("might_contain", "hello", True),   # was added — must return True
                Op("might_contain", "world", True),   # was added — must return True
                Op("might_contain", "foo", True),     # was added — must return True
                Op("might_contain", "bar", None),     # not added — may be True or False
                Op("might_contain", "baz", None),     # not added — may be True or False
            ]),
            Problem(100, 2, [
                Op("add", "a", None),
                Op("add", "b", None),
                Op("might_contain", "a", True),
                Op("might_contain", "b", True),
            ]),
            # Problem(???, ???, [Op("???", "???", ???)]),  # add your own
        ]

    def run(self, bloom_filter_class) -> List[Tuple[Op, Optional[bool], bool]]:
        bf = bloom_filter_class(self.size, self.num_hashes)
        results = []
        for op in self.ops:
            if op.kind == "add":
                bf.add(op.item)
                actual = None
                passed = True
            else:  # might_contain
                actual = bf.might_contain(op.item)
                # If expected is None, the item was not added; false positives are allowed.
                passed = op.expected is None or actual == op.expected
            results.append((op, actual, passed))
        return results
