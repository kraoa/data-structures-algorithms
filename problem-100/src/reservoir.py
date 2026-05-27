"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def build_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


@dataclass
class Problem:
    values: List[int]
    trials: int

    def run(self, sampler_class) -> Tuple[bool, str]:
        head = build_list(self.values)
        sampler = sampler_class(head)
        results = [sampler.get_random() for _ in range(self.trials)]
        value_set = set(self.values)
        all_valid = all(r in value_set for r in results)
        if not all_valid:
            return False, f"got value outside {value_set}"
        if len(self.values) > 1 and self.trials >= 100:
            seen = set(results)
            if seen != value_set:
                return False, f"not all values appeared: missing {value_set - seen}"
        return True, "ok"


class Reservoir:
    @staticmethod
    def get_test_cases() -> List[Problem]:
        return [
            Problem(values=[1, 2, 3], trials=300),
            Problem(values=[1], trials=10),
            # Problem(values=???, trials=???),  # add your own
        ]

    @staticmethod
    def run(solver_class) -> List[Tuple[Problem, str, bool]]:
        results = []
        for prob in Reservoir.get_test_cases():
            passed, msg = prob.run(solver_class)
            results.append((prob, msg, passed))
        return results
