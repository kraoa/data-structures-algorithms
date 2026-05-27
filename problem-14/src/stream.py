"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str               # "addNum" or "findMedian"
    num: Optional[int]      # only used for "addNum"
    expected: Optional[float]  # expected return value for "findMedian"; None for "addNum"

    def __repr__(self) -> str:
        if self.kind == "addNum":
            return f"addNum({self.num})"
        return f"findMedian() -> {self.expected}"


class Problem:
    """
    Design a data structure that supports:
      addNum(num)   — add an integer to the data stream.
      findMedian()  — return the median of all elements added so far.
                      If the count is even, the median is the average of the
                      two middle elements.

    Example:
        addNum(1), addNum(2) → findMedian() = 1.5
        addNum(3)            → findMedian() = 2.0

    Aim for O(log n) addNum and O(1) findMedian using two heaps.
    """

    def __init__(self, ops: List[Op]):
        self.ops = ops

    def run(self, finder) -> List[Tuple[Op, float, bool]]:
        """
        Replays all ops against finder.
        finder must expose .addNum(num: int) -> None
                       and .findMedian() -> float.
        Returns (op, actual, passed) for every findMedian call.
        """
        results = []
        for op in self.ops:
            if op.kind == "addNum":
                finder.addNum(op.num)
            else:
                actual = finder.findMedian()
                passed = abs(actual - op.expected) < 1e-9
                results.append((op, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem([
                Op("addNum", 1,    None),
                Op("addNum", 2,    None),
                Op("findMedian", None, 1.5),
                Op("addNum", 3,    None),
                Op("findMedian", None, 2.0),
            ]),
            Problem([
                Op("addNum", 6,    None),
                Op("findMedian", None, 6.0),
                Op("addNum", 10,   None),
                Op("findMedian", None, 8.0),
                Op("addNum", 2,    None),
                Op("findMedian", None, 6.0),
                Op("addNum", 6,    None),
                Op("findMedian", None, 6.0),
            ]),
            Problem([
                Op("addNum", -1,   None),
                Op("addNum", -2,   None),
                Op("findMedian", None, -1.5),
                Op("addNum", -3,   None),
                Op("findMedian", None, -2.0),
                Op("addNum", -4,   None),
                Op("findMedian", None, -2.5),
            ]),
            # Problem([...]),  # add your own
        ]
