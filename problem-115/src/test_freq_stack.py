"""Tests for the freq_stack driver. Must pass out of the box."""

import unittest
from typing import List, Optional

from freq_stack import Problem, Op


class _NaiveFreqStack:
    """Reference — O(n) per pop; scans the whole internal stack for max frequency."""

    def __init__(self) -> None:
        self._stack: List[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)

    def pop(self) -> int:
        freq: dict = {}
        for v in self._stack:
            freq[v] = freq.get(v, 0) + 1
        max_f = max(freq.values())
        # Find the rightmost (most recently pushed) element with max frequency.
        for i in range(len(self._stack) - 1, -1, -1):
            if freq[self._stack[i]] == max_f:
                return self._stack.pop(i)
        return -1  # unreachable


class TestFreqStackDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            ref = _NaiveFreqStack()
            for op in problem.ops:
                if op.kind == "push":
                    ref.push(op.val)
                else:
                    result = ref.pop()
                    self.assertEqual(
                        op.expected,
                        result,
                        msg=f"pop(): stored expected={op.expected}, brute force={result}",
                    )

    def test_run_returns_correct_structure(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(_NaiveFreqStack)
            self.assertEqual(len(results), len(problem.ops))

    def test_run_passes_with_reference(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(_NaiveFreqStack)
            for op, actual, passed in results:
                self.assertTrue(passed, msg=f"Reference failed: op={op}, actual={actual}")


if __name__ == "__main__":
    unittest.main()
