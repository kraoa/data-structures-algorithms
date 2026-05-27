"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


@dataclass
class TestCase:
    values: List[int]
    k: int
    expected: List[int]


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(values=[1, 2, 3, 4, 5], k=2, expected=[2, 1, 4, 3, 5]),
            TestCase(values=[1, 2, 3, 4, 5], k=3, expected=[3, 2, 1, 4, 5]),
            TestCase(values=[1, 2, 3, 4, 5], k=1, expected=[1, 2, 3, 4, 5]),
            TestCase(values=[1, 2], k=2, expected=[2, 1]),
            TestCase(values=[1], k=1, expected=[1]),
            # TestCase(values=???, k=???, expected=???),  # add your own
        ]

    @staticmethod
    def build_list(values: List[int]) -> Optional[ListNode]:
        if not values:
            return None
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        result = []
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            head = Problem.build_list(list(tc.values))
            result_head = solver.reverse_k_group(head, tc.k)
            actual = Problem.to_list(result_head)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(values: List[int], k: int) -> List[int]:
        """Convert to list, reverse chunks of k, leave trailing partial group unchanged."""
        result = list(values)
        i = 0
        while i + k <= len(result):
            result[i: i + k] = result[i: i + k][::-1]
            i += k
        return result
