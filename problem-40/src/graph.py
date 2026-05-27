"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    times: List[List[int]]  # [source, target, weight] directed edges
    n: int                  # number of nodes, labeled 1..n
    k: int                  # source node
    expected: int           # minimum time for signal to reach all nodes; -1 if unreachable


class Problem:
    """
    A signal is sent from node k in a directed, weighted graph of n nodes.
    times[i] = [u, v, w] means sending from u to v takes w milliseconds.
    Return the minimum time for the signal to reach every node, or -1 if any
    node is unreachable from k.

    Example: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2 → 2
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        """
        Calls solver.network_delay_time(times, n, k) for each test case.
        solver must expose .network_delay_time(times, n, k) -> int.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.network_delay_time([list(e) for e in tc.times], tc.n, tc.k)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[2,1,1],[2,3,1],[3,4,1]], 4, 2,  2),  # LeetCode example 1
            TestCase([[1,2,1]],                 2, 1,  1),  # LeetCode example 2
            TestCase([[1,2,1]],                 2, 2, -1),  # source cannot reach node 1
            TestCase([],                        1, 1,  0),  # single node
            TestCase([[1,2,9],[1,3,1],[3,2,1]], 3, 1,  2),  # indirect path is cheaper
            # TestCase([[???]], ?, ?, ??),  # add your own
        ]
