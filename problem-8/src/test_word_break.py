"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest
from segmentation import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)
        # Uncomment once Solver is implemented:
        # failures = [(tc.s, actual) for tc, actual, passed in problem.run(solver) if not passed]
        # self.assertEqual(failures, [], f"failing cases: {failures}")

    # def test_no_segmentation(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.word_break("abcdef", {"abc", "gh"}), [])

    # def test_single_word(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.word_break("a", {"a"}), ["a"])

    # def test_all_sentences_valid(self) -> None:
    #     """Every returned sentence must concatenate to s using only dict words."""
    #     solver = Solver()
    #     word_dict = {"cat", "cats", "and", "sand", "dog"}
    #     result = solver.word_break("catsanddog", word_dict)
    #     for sentence in result:
    #         words = sentence.split()
    #         self.assertEqual("".join(words), "catsanddog")
    #         self.assertTrue(all(w in word_dict for w in words))


if __name__ == "__main__":
    unittest.main()
