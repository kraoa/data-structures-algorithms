"""Driver tests — all must pass out of the box."""

import unittest
from subarray import Problem, TestCase


class TestSubarray(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: list) -> int:
        """O(n²): check all subarrays."""
        best = nums[0]
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                best = max(best, product)
        return best

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._brute_force(tc.nums))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"max_product": lambda self, n: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
