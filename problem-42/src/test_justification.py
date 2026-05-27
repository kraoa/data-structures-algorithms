"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from formatting import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic(self) -> None:
    #     solver = Solver()
    #     result = solver.full_justify(
    #         ["This","is","an","example","of","text","justification."], 16)
    #     self.assertEqual(result, ["This    is    an","example  of text","justification.  "])

    # def test_all_lines_correct_width(self) -> None:
    #     solver = Solver()
    #     result = solver.full_justify(["a", "b", "c"], 5)
    #     for line in result:
    #         self.assertEqual(len(line), 5)

    # def test_last_line_left_justified(self) -> None:
    #     solver = Solver()
    #     result = solver.full_justify(["What","must","be","acknowledgment","shall","be"], 16)
    #     self.assertEqual(result[-1], "shall be        ")

    # def test_single_word_line(self) -> None:
    #     # A line containing only one word must be left-justified with trailing spaces.
    #     solver = Solver()
    #     result = solver.full_justify(["acknowledgment"], 16)
    #     self.assertEqual(result, ["acknowledgment  "])


if __name__ == "__main__":
    unittest.main()
