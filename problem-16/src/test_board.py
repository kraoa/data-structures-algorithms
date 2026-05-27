"""Tests for Problem. Verifies the is_valid_solution checker."""

import unittest
from board import Problem


class ProblemTest(unittest.TestCase):

    def test_valid_4queens_solution(self) -> None:
        sol = [".Q..", "...Q", "Q...", "..Q."]
        self.assertTrue(Problem.is_valid_solution(sol, 4))

    def test_invalid_same_column(self) -> None:
        sol = ["Q...", "Q...", "....", "...."]
        self.assertFalse(Problem.is_valid_solution(sol, 4))

    def test_invalid_same_diagonal(self) -> None:
        sol = ["Q...", ".Q..", "....", "...."]
        self.assertFalse(Problem.is_valid_solution(sol, 4))

    def test_invalid_wrong_queen_count(self) -> None:
        sol = ["Q...", "....", "....", "...."]
        self.assertFalse(Problem.is_valid_solution(sol, 4))

    def test_invalid_wrong_size(self) -> None:
        sol = ["Q.", ".Q"]
        self.assertFalse(Problem.is_valid_solution(sol, 4))

    def test_valid_1queen(self) -> None:
        self.assertTrue(Problem.is_valid_solution(["Q"], 1))

    def test_invalid_bad_character(self) -> None:
        sol = ["Q...", "X...", "....", "...."]
        self.assertFalse(Problem.is_valid_solution(sol, 4))


if __name__ == "__main__":
    unittest.main()
