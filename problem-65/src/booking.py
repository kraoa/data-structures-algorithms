"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Op:
    start: int
    end: int
    expected: int   # max k-booking count after this book() call


@dataclass
class Problem:
    ops: List[Op]

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            Problem(ops=[
                Op(10, 20, 1),
                Op(50, 60, 1),
                Op(10, 40, 2),
                Op(5, 15, 3),
                Op(5, 10, 3),
                Op(25, 55, 3),
            ]),
            # Problem(ops=[...]),  # add your own
        ]

    def run(self, solver_class) -> List[tuple]:
        """Create MyCalendarThree(), call book for each op, collect results."""
        calendar = solver_class()
        results = []
        for op in self.ops:
            actual = calendar.book(op.start, op.end)
            passed = actual == op.expected
            results.append((op, actual, passed))
        return results

    @staticmethod
    def brute_force_max_k(bookings: List[tuple]) -> int:
        """Difference-array sweep after adding all bookings so far; O(n^2) total."""
        diff: dict[int, int] = {}
        for s, e in bookings:
            diff[s] = diff.get(s, 0) + 1
            diff[e] = diff.get(e, 0) - 1
        current = max_k = 0
        for t in sorted(diff):
            current += diff[t]
            if current > max_k:
                max_k = current
        return max_k

    @staticmethod
    def reference_sequence(ops: List[Op]) -> List[int]:
        """Return the expected max-k after each booking using the brute-force sweep."""
        bookings: list[tuple] = []
        results = []
        for op in ops:
            bookings.append((op.start, op.end))
            results.append(Problem.brute_force_max_k(bookings))
        return results
