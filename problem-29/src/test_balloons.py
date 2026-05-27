"""Driver tests — all must pass out of the box."""

import unittest
from balloons import Problem, TestCase


class TestBalloons(unittest.TestCase):

    @staticmethod
    def _brute_force(nums: list) -> int:
        """Try all burst orderings; valid only for small inputs (≤8 balloons)."""
        def helper(remaining: list) -> int:
            if not remaining:
                return 0
            best = 0
            for i in range(len(remaining)):
                left = remaining[i - 1] if i > 0 else 1
                right = remaining[i + 1] if i < len(remaining) - 1 else 1
                coins = left * remaining[i] * right
                new_rem = remaining[:i] + remaining[i + 1:]
                best = max(best, coins + helper(new_rem))
            return best

        return helper(list(nums))

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._brute_force(tc.nums))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"max_coins": lambda self, n: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
