"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    s: str
    expected: int  # number of valid decodings


class Problem:
    """
    A string of digits encodes letters: '1'→'A', '2'→'B', …, '26'→'Z'.
    Return the number of ways to decode the string s.

    Rules:
      - '0' cannot be decoded on its own; it must pair with a '1' or '2'.
      - Leading '0' makes a grouping invalid (e.g. "06" is not "F").

    Example: "12" → 2  ("AB" from "1"+"2", or "L" from "12")
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.num_decodings(s) for each test case.
        solver must expose .num_decodings(s: str) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.num_decodings(tc.s)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("12",   2),   # "AB" or "L"
            TestCase("226",  3),   # "BZ", "VF", "BBF"
            TestCase("06",   0),   # leading zero in a group
            TestCase("0",    0),
            TestCase("10",   1),   # only "J"
            TestCase("11106", 2),
            TestCase("1",    1),
            TestCase("27",   1),   # 27 > 26, so only "BG"
            # TestCase("???", ?),  # add your own
        ]
