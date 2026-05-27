"""Tests for Problem. Verifies test cases against a sort-based reference finder."""

import unittest
from stream import Problem


class _BruteForceMedianFinder:
    """O(n log n) reference: keep a sorted list and pick the middle element(s)."""

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        self._nums.append(num)

    def findMedian(self) -> float:
        s = sorted(self._nums)
        n = len(s)
        if n % 2 == 0:
            return (s[n // 2 - 1] + s[n // 2]) / 2.0
        return float(s[n // 2])


class ProblemTest(unittest.TestCase):

    def test_all_cases_pass_with_brute_force(self) -> None:
        """Every stored expected value must agree with the sort-based reference."""
        for i, problem in enumerate(Problem.get_test_cases()):
            finder = _BruteForceMedianFinder()
            results = problem.run(finder)
            failures = [(op, actual) for op, actual, passed in results if not passed]
            self.assertEqual(failures, [], f"test case {i + 1} failures: {failures}")

    def test_run_skips_addnum_ops(self) -> None:
        """run() should only return results for findMedian calls."""
        from stream import Op
        problem = Problem([
            Op("addNum", 5, None),
            Op("addNum", 3, None),
        ])
        results = problem.run(_BruteForceMedianFinder())
        self.assertEqual(results, [])

    def test_median_odd_count(self) -> None:
        from stream import Op
        problem = Problem([
            Op("addNum", 1, None),
            Op("addNum", 2, None),
            Op("addNum", 3, None),
            Op("findMedian", None, 2.0),
        ])
        results = problem.run(_BruteForceMedianFinder())
        _, actual, passed = results[0]
        self.assertTrue(passed, f"expected 2.0, got {actual}")

    def test_median_even_count(self) -> None:
        from stream import Op
        problem = Problem([
            Op("addNum", 1, None),
            Op("addNum", 2, None),
            Op("findMedian", None, 1.5),
        ])
        results = problem.run(_BruteForceMedianFinder())
        _, actual, passed = results[0]
        self.assertTrue(passed, f"expected 1.5, got {actual}")


if __name__ == "__main__":
    unittest.main()
