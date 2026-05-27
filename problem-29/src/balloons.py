"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: int  # maximum coins obtainable


class Problem:
    """
    You have n balloons numbered 0..n-1, each with a value nums[i].
    Bursting balloon i earns nums[i-1] * nums[i] * nums[i+1] coins
    (treat out-of-bounds neighbours as 1). Burst all balloons and
    return the maximum total coins.

    Example: [3,1,5,8] → 167
             Burst 1 (3×1×5=15), burst 5 (3×5×8=120), burst 3 (1×3×8=24),
             burst 8 (1×8×1=8): 15+120+24+8=167.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.max_coins(list(tc.nums))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([3, 1, 5, 8], 167),
            TestCase([1, 5], 10),         # burst 1 (1×1×5=5), burst 5 (1×5×1=5): 10
            TestCase([1], 1),
            TestCase([3, 1, 5], 35),      # burst 1 (3×1×5=15), burst 3 (1×3×5=15), burst 5 (1×5×1=5): 35
            TestCase([5], 5),
            # TestCase([...], ?),         # add your own
        ]
