"""Driver tests — all must pass out of the box."""

import unittest
from selection import Problem, TestCase


class TestSelection(unittest.TestCase):

    @staticmethod
    def _sort_select(nums: list, k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    def test_expected_values_match_sort(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._sort_select(tc.nums, tc.k))

    def test_run_passes_copy_to_solver(self) -> None:
        """Solver must not be able to corrupt stored test cases."""
        tcs = Problem.get_test_cases()
        originals = [list(tc.nums) for tc in tcs]
        problem = Problem(tcs)
        problem.run(type("S", (), {"find_kth_largest": lambda self, n, k: sorted(n)[0]})())
        for tc, original in zip(tcs, originals):
            self.assertEqual(tc.nums, original)

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"find_kth_largest": lambda self, n, k: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
