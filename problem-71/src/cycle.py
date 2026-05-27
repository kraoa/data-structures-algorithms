"""Read this first."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


@dataclass
class TestCase:
    values: List[int]
    cycle_pos: int      # index of node that tail points to; -1 means no cycle
    expected: int       # expected cycle entry index; -1 if no cycle


class Problem:
    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(values=[3, 2, 0, -4], cycle_pos=1, expected=1),
            TestCase(values=[1, 2], cycle_pos=0, expected=0),
            TestCase(values=[1], cycle_pos=-1, expected=-1),
            TestCase(values=[1, 2, 3, 4, 5], cycle_pos=2, expected=2),
            # TestCase(values=???, cycle_pos=???, expected=???),  # add your own
        ]

    @staticmethod
    def build_list(
        values: List[int], cycle_pos: int
    ) -> tuple[Optional[ListNode], Dict[int, int]]:
        """Build linked list with optional cycle; return (head, id_to_index map)."""
        if not values:
            return None, {}
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if cycle_pos >= 0:
            nodes[-1].next = nodes[cycle_pos]
        id_to_index = {id(node): i for i, node in enumerate(nodes)}
        return nodes[0], id_to_index

    @staticmethod
    def run(solver) -> List[tuple]:
        results = []
        for tc in Problem.get_test_cases():
            head, id_to_index = Problem.build_list(tc.values, tc.cycle_pos)
            result_node = solver.detect_cycle(head)
            if result_node is None:
                actual = -1
            else:
                actual = id_to_index.get(id(result_node), -1)
            passed = actual == tc.expected
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
        """Visited-set approach: O(n) time, O(n) space."""
        visited: set[int] = set()
        node = head
        while node is not None:
            if id(node) in visited:
                return node
            visited.add(id(node))
            node = node.next
        return None
