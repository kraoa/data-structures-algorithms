"""Read this first."""

from typing import List, Optional, Tuple


class ListNode:
    """A node in a singly-linked list."""

    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def from_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list of integers."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """Flatten a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestCase:
    def __init__(self, lists: List[List[int]], expected: List[int]):
        self.lists = lists        # k sorted lists represented as Python lists
        self.expected = expected  # expected merged output

    def make_nodes(self) -> List[Optional[ListNode]]:
        """Convert each Python list to a linked-list head node."""
        return [from_list(lst) for lst in self.lists]


class Problem:
    """
    Merge k sorted linked lists into one sorted linked list.

    Naive approach: merge lists one by one in O(kN).
    Optimal approach: use a min-heap for O(N log k),
    where N is the total number of nodes across all lists.
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, List[int], bool]]:
        """
        Calls solver.merge_k_lists(lists) for each test case.
        solver must expose .merge_k_lists(lists: List[Optional[ListNode]])
                                         -> Optional[ListNode].
        Returns (test_case, actual_as_python_list, passed).
        """
        results = []
        for tc in self.test_cases:
            head = solver.merge_k_lists(tc.make_nodes())
            actual = to_list(head)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
            TestCase([],                              []),   # zero lists
            TestCase([[]],                            []),   # one empty list
            TestCase([[1]],                           [1]),  # one single-element list
            TestCase([[1, 2], [3, 4]],                [1, 2, 3, 4]),
            TestCase([[-1, 0, 1], [-2, 0, 2]],        [-2, -1, 0, 0, 1, 2]),
            # TestCase([...], [...]),                         # add your own
        ]
