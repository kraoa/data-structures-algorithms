"""Read this first."""

import copy
from dataclasses import dataclass, field
from itertools import combinations
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: List[List[int]]  # sorted list of sorted triplets


class Problem:
    """
    Given an integer array nums, return all unique triplets [a, b, c] such that
    a + b + c == 0. The solution set must not contain duplicate triplets.

    Example: nums = [-1, 0, 1, 2, -1, -4] -> [[-1,-1,2], [-1,0,1]]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[List[int]], bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.three_sum(list(tc.nums))
            passed = self._normalize(actual) == self._normalize(tc.expected)
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def _normalize(triplets: List[List[int]]) -> List[List[int]]:
        return sorted(sorted(t) for t in triplets)

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # LeetCode example 1
            TestCase([0, 1, 1],             []),                            # LeetCode example 2
            TestCase([0, 0, 0],             [[0, 0, 0]]),                   # LeetCode example 3
            TestCase([-2, 0, 0, 2, 2],      [[-2, 0, 2]]),
            TestCase([],                    []),                            # empty input
            TestCase([0],                   []),                            # too short
            # TestCase([???], [???]),  # add your own
        ]
