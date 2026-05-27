"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    coins: List[int]
    amount: int
    expected: int  # minimum number of coins, or -1 if impossible


class Problem:
    """
    Given coin denominations and a target amount, return the minimum number
    of coins needed to make up that amount. Return -1 if it is impossible.
    You may use each coin denomination an unlimited number of times.

    Example: coins = [1, 5, 11], amount = 15 → 3  (5 + 5 + 5)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.coin_change(coins, amount) for each test case.
        solver must expose .coin_change(coins: List[int], amount: int) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.coin_change(list(tc.coins), tc.amount)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([1, 2, 5], 11,  3),   # LeetCode example 1: 5+5+1
            TestCase([2],       3,  -1),   # LeetCode example 2: impossible
            TestCase([1],       0,   0),   # LeetCode example 3: zero amount
            TestCase([1, 5, 11], 15, 3),   # greedy fails (5+5+5), 11+1+1+1+1=5, 5+5+5=3 ✓
            TestCase([2, 5, 10, 1], 27, 4),
            TestCase([186, 419, 83, 408], 6249, 20),
            # TestCase([...], ?, ?),  # add your own
        ]
