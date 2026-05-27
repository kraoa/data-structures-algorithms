"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: bool   # True if Player 1 can win or tie


class Problem:
    """
    Two players take turns picking a number from either end of an integer array.
    Player 1 goes first. The player with the higher total score wins; ties count
    as a win for Player 1. Return True if Player 1 can guarantee a win or tie.

    Example: nums = [1, 5, 2] → False  (Player 2 always scores ≥ Player 1)
             nums = [1, 5, 233, 7] → True
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, bool, bool]]:
        """
        Calls solver.predict_the_winner(nums) for each test case.
        solver must expose .predict_the_winner(nums: List[int]) -> bool.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.predict_the_winner(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 5, 2],          False),  # LeetCode example 1
            TestCase([1, 5, 233, 7],     True),   # LeetCode example 2
            TestCase([1, 2],             True),   # Player 1 picks 2
            TestCase([1],                True),   # trivially, P1 gets everything
            TestCase([1, 3, 1],          False),  # P2 always does better
            TestCase([0, 0],             True),   # tie → True
            # TestCase([???], ???),  # add your own
        ]
