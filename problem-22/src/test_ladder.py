"""Driver tests — all must pass out of the box."""

import unittest
from collections import deque
from ladder import Problem, TestCase


class TestLadder(unittest.TestCase):

    @staticmethod
    def _bfs(begin: str, end: str, word_list: list) -> int:
        """BFS reference: one level = one transformation step."""
        word_set = set(word_list)
        if end not in word_set:
            return 0
        if begin == end:
            return 1
        queue = deque([(begin, 1)])
        visited = {begin}
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate = word[:i] + c + word[i + 1:]
                    if candidate == end:
                        return length + 1
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, length + 1))
        return 0

    def test_expected_values_match_bfs(self) -> None:
        for tc in Problem.get_test_cases():
            self.assertEqual(tc.expected, self._bfs(tc.begin_word, tc.end_word, tc.word_list))

    def test_run_returns_correct_shape(self) -> None:
        problem = Problem(Problem.get_test_cases())
        stub = type("S", (), {"ladder_length": lambda self, b, e, w: 0})()
        for tc, actual, passed in problem.run(stub):
            self.assertIsInstance(tc, TestCase)
            self.assertIsInstance(actual, int)
            self.assertIsInstance(passed, bool)


if __name__ == "__main__":
    unittest.main()
