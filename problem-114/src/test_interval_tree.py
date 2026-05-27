"""Tests for the interval_tree driver. Must pass out of the box."""

import unittest
from interval_tree import Problem, Op


class FlatIntervalTree:
    """Reference implementation — stores all intervals in a list, O(n) per query."""

    def __init__(self) -> None:
        self._intervals: list = []

    def insert(self, lo: int, hi: int) -> None:
        self._intervals.append((lo, hi))

    def query(self, point: int) -> int:
        return sum(1 for lo, hi in self._intervals if lo <= point <= hi)


class TestIntervalTreeDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            ref = FlatIntervalTree()
            for op in problem.ops:
                if op.kind == "insert":
                    ref.insert(op.lo, op.hi)
                else:
                    result = ref.query(op.lo)
                    self.assertEqual(
                        op.expected,
                        result,
                        msg=f"query({op.lo}): stored expected={op.expected}, brute force={result}",
                    )

    def test_run_returns_correct_structure(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(FlatIntervalTree)
            self.assertEqual(len(results), len(problem.ops))

    def test_run_passes_with_reference(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(FlatIntervalTree)
            for op, actual, passed in results:
                self.assertTrue(passed, msg=f"Reference failed: op={op}, actual={actual}")


if __name__ == "__main__":
    unittest.main()
