"""Driver tests — all must pass out of the box."""

import unittest
from collections import deque
from jumps import Problem, TestCase


class TestJumps(unittest.TestCase):

    @staticmethod
    def _bfs(nums: list) -> int:
        """BFS reference: each BFS level is one additional jump."""
        n = len(nums)
        if n == 1:
            return 0
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        jumps = 0
        while queue:
            jumps += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    if j == n - 1:
                        return jumps
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)
        return -1

    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._bfs(tc.nums))

    def test_single_element_needs_zero_jumps(self) -> None:
        self.assertEqual(self._bfs([1]), 0)

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"min_jumps": lambda self, n: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
