"""Tests for the Problem driver (range_queries.py)."""

import unittest
from range_queries import Problem


class TestRangeQueries(unittest.TestCase):
    def test_expected_values_match_naive(self) -> None:
        for problem in Problem.get_test_cases():
            results = Problem.naive_run(problem)
            for op, actual, passed in results:
                self.assertTrue(
                    passed,
                    msg=f"sum_range({op.i},{op.j}): got {actual}, expected {op.expected}",
                )

    def test_naive_update_then_query(self) -> None:
        from range_queries import Op, Problem as P
        problem = P(nums=[5, 5, 5], ops=[
            Op("update", 1, None, 10, None),
            Op("sum_range", 0, 2, None, 20),
        ])
        results = P.naive_run(problem)
        _, actual, passed = results[0]
        self.assertTrue(passed)
        self.assertEqual(actual, 20)

    def test_naive_single_element(self) -> None:
        from range_queries import Op, Problem as P
        problem = P(nums=[42], ops=[Op("sum_range", 0, 0, None, 42)])
        results = P.naive_run(problem)
        _, actual, _ = results[0]
        self.assertEqual(actual, 42)


if __name__ == "__main__":
    unittest.main()
