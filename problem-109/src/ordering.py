"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    nums: List[int]
    expected: str


class Ordering:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([10, 2], "210"),
            TestCase([3, 30, 34, 5, 9], "9534330"),
            TestCase([1], "1"),
            TestCase([10], "10"),
            TestCase([0, 0], "0"),
            TestCase([824,938,1399,5607,6973,5703,9609,4398,8247],
                     "9609938824824769735703560743981399"),
            # TestCase("???", "??"),  # add your own
        ]

    @staticmethod
    def run(solver) -> List[Tuple[TestCase, str, bool]]:
        results = []
        for tc in Ordering.get_test_cases():
            actual = solver.largest_number(list(tc.nums))
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results
