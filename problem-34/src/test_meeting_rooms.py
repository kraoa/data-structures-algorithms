"""Tests for Solver. Assertions are commented out until Solver is implemented."""

import unittest
from intervals import Problem
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        problem = Problem(Problem.get_test_cases())
        solver = Solver()
        problem.run(solver)

    # def test_basic_overlap(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_meeting_rooms([[0,30],[5,10],[15,20]]), 2)

    # def test_no_overlap(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_meeting_rooms([[7,10],[2,4]]), 1)

    # def test_empty(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.min_meeting_rooms([]), 0)

    # def test_back_to_back_reuses_room(self) -> None:
    #     # Meeting ending at 10 and starting at 10 do NOT overlap.
    #     solver = Solver()
    #     self.assertEqual(solver.min_meeting_rooms([[0,10],[10,20]]), 1)


if __name__ == "__main__":
    unittest.main()
