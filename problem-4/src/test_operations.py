"""Tests for Problem. Verifies that the test runner correctly detects pass and fail."""

import unittest
from operations import Op, Problem


class _FixedCache:
    """Stub cache that returns a pre-set sequence of values for get."""

    def __init__(self, answers: list):
        self._answers = iter(answers)

    def get(self, key: int) -> int:
        return next(self._answers)

    def put(self, key: int, value: int) -> None:
        pass


class _AlwaysMiss:
    """Stub cache that always returns -1 for get."""

    def get(self, key: int) -> int:
        return -1

    def put(self, key: int, value: int) -> None:
        pass


class ProblemTest(unittest.TestCase):

    def test_run_all_pass(self) -> None:
        problem = Problem(2, [
            Op("put", 1, 1,  None),
            Op("get", 1, None, 42),
            Op("get", 2, None, -1),
        ])
        results = problem.run(_FixedCache([42, -1]))
        self.assertEqual(len(results), 2)
        self.assertTrue(all(passed for _, _, passed in results))

    def test_run_detects_failure(self) -> None:
        problem = Problem(1, [
            Op("get", 99, None, 5),
        ])
        results = problem.run(_AlwaysMiss())
        _, actual, passed = results[0]
        self.assertFalse(passed)
        self.assertEqual(actual, -1)

    def test_put_ops_not_in_results(self) -> None:
        problem = Problem(1, [
            Op("put", 1, 1, None),
            Op("put", 2, 2, None),
        ])
        results = problem.run(_AlwaysMiss())
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
