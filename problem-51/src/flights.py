"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    n: int                  # number of cities, labeled 0..n-1
    flights: List[List[int]]  # [from, to, price]
    src: int
    dst: int
    k: int                  # maximum number of stops (not edges — edges = k+1)
    expected: int            # cheapest price; -1 if unreachable within k stops


class Problem:
    """
    There are n cities connected by directed flights. Each flight [u, v, w]
    goes from city u to city v with price w. Find the cheapest price from src
    to dst using at most k stops. Return -1 if no such route exists.

    Example: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
             src=0, dst=3, k=1 → 700  (0→1→3)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.find_cheapest_price(n, flights, src, dst, k) for each test case.
        solver must expose
          .find_cheapest_price(n, flights, src, dst, k) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.find_cheapest_price(
                tc.n, [list(f) for f in tc.flights], tc.src, tc.dst, tc.k
            )
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
                     0, 3, 1, 700),  # LeetCode example 1: 0→1→3
            TestCase(3, [[0,1,100],[1,2,100],[0,2,500]],
                     0, 2, 1, 200),  # LeetCode example 2: 0→1→2
            TestCase(3, [[0,1,100],[1,2,100],[0,2,500]],
                     0, 2, 0, 500),  # LeetCode example 3: direct only
            TestCase(1, [], 0, 0, 0, 0),  # trivial: src == dst
            TestCase(3, [[0,1,100],[1,2,100]], 0, 2, 1, 200),  # exact k stops
            TestCase(3, [[0,1,100],[1,2,100]], 0, 2, 0, -1),   # not enough stops
            # TestCase(??, [[???]], ??, ??, ??, ??),  # add your own
        ]
