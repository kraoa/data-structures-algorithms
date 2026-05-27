"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    n: int
    expected_count: int  # number of distinct valid solutions


class Problem:
    """
    Place n queens on an n×n board so that no two queens attack each other
    (no shared row, column, or diagonal). Return all distinct solutions.

    Each solution is represented as a list of n strings of length n,
    where 'Q' marks a queen and '.' marks an empty cell.

    Known counts: n=1→1, n=4→2, n=5→10, n=6→4, n=8→92.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def is_valid_solution(board: List[str], n: int) -> bool:
        """
        Returns True iff board is a valid n-queens placement:
          - n×n grid using only 'Q' and '.'
          - Exactly n queens placed
          - No two queens share a row, column, or diagonal
        """
        if len(board) != n or not all(len(row) == n for row in board):
            return False
        queens = [(r, c) for r, row in enumerate(board) for c, ch in enumerate(row) if ch == "Q"]
        if any(ch not in "Q." for row in board for ch in row):
            return False
        if len(queens) != n:
            return False
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    return False
        return True

    def run(self, solver) -> List[Tuple[TestCase, List[List[str]], bool]]:
        """
        Calls solver.solve_n_queens(n) for each test case.
        solver must expose .solve_n_queens(n: int) -> List[List[str]].
        Returns (test_case, solutions, passed).
        passed requires: every solution is valid, no duplicates, and the
        count matches expected_count.
        """
        results = []
        for tc in self.test_cases:
            solutions = solver.solve_n_queens(tc.n)
            all_valid = all(self.is_valid_solution(sol, tc.n) for sol in solutions)
            no_dupes = len(solutions) == len({tuple(sol) for sol in solutions})
            right_count = len(solutions) == tc.expected_count
            results.append((tc, solutions, all_valid and no_dupes and right_count))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(1,  1),
            TestCase(4,  2),
            TestCase(5, 10),
            TestCase(6,  4),
            # TestCase(8, 92),  # uncomment if your solver is fast enough
        ]
