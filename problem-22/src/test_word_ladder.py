"""Solver stub tests — uncomment assertions as you implement."""

import unittest
from ladder import Problem
from solver import Solver


class TestWordLadder(unittest.TestCase):

    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5
    #     )

    # def test_no_path(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(
    #         solver.ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]), 0
    #     )

    # def test_end_word_not_reachable_in_one_step(self) -> None:
    #     # "hot" and "dog" differ by 2 letters — can't transform directly.
    #     solver = Solver()
    #     self.assertEqual(solver.ladder_length("hot", "dog", ["hot", "dog"]), 0)


if __name__ == "__main__":
    unittest.main()
