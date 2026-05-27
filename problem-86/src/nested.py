"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple, Union


class NestedInteger:
    def __init__(self, val: Optional[int] = None) -> None:
        self._val = val
        self._list: List["NestedInteger"] = []

    def isInteger(self) -> bool:
        return self._val is not None

    def getInteger(self) -> int:
        return self._val  # type: ignore[return-value]

    def getList(self) -> List["NestedInteger"]:
        return self._list

    @staticmethod
    def from_list(data: Union[int, list]) -> "NestedInteger":
        """Build from a Python int or arbitrarily nested list."""
        if isinstance(data, int):
            ni = NestedInteger(data)
            return ni
        ni = NestedInteger()
        for item in data:
            ni._list.append(NestedInteger.from_list(item))
        return ni


@dataclass
class Op:
    kind: str              # "hasNext" or "next"
    expected: Union[bool, int]


class Problem:
    def __init__(self, nested_list_data: list, ops: List[Op]) -> None:
        self.nested_list_data = nested_list_data
        self.ops = ops

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(
                [[1, 1], 2, [1, 1]],
                [
                    Op("hasNext", True),
                    Op("next", 1),
                    Op("hasNext", True),
                    Op("next", 1),
                    Op("hasNext", True),
                    Op("next", 2),
                    Op("hasNext", True),
                    Op("next", 1),
                    Op("hasNext", True),
                    Op("next", 1),
                    Op("hasNext", False),
                ],
            ),
            Problem(
                [1, [4, [6]]],
                [
                    Op("hasNext", True),
                    Op("next", 1),
                    Op("hasNext", True),
                    Op("next", 4),
                    Op("hasNext", True),
                    Op("next", 6),
                    Op("hasNext", False),
                ],
            ),
            # Problem("???", []),  # add your own
        ]

    def run(self, iterator_class) -> List[Tuple[Op, Union[bool, int], bool]]:
        ni_list = [NestedInteger.from_list(item) for item in self.nested_list_data]
        iterator = iterator_class(ni_list)
        results = []
        for op in self.ops:
            if op.kind == "hasNext":
                actual = iterator.hasNext()
            else:
                actual = iterator.next()
            passed = actual == op.expected
            results.append((op, actual, passed))
        return results
