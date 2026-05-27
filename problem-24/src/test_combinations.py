"""Driver tests — all must pass out of the box."""

import unittest
from combinations import Problem, TestCase


class TestCombinations(unittest.TestCase):

    @staticmethod
    def _backtrack(candidates: list, target: int) -> list:
        """Reference: recursive backtracking, sorted output."""
        result = []

        def bt(start: int, current: list, remaining: int) -> None:
            if remaining == 0:
                result.append(sorted(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    current.append(candidates[i])
                    bt(i, current, remaining - candidates[i])
                    current.pop()

        bt(0, [], target)
        return sorted(result)

    def test_expected_values_match_backtrack(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._backtrack(tc.candidates, tc.target))

    def test_run_normalises_solver_output(self) -> None:
        """run() sorts each combination and the outer list."""
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"combination_sum": lambda self, c, t: []})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, list)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
