"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str            # "put", "get", "remove"
    key: int
    value: Optional[int]  # used for "put"; None otherwise
    expected: Optional[int]  # None for "put"/"remove"; int for "get"


@dataclass
class Problem:
    ops: List[Op]


class HashMap:
    @staticmethod
    def get_test_cases() -> List[Problem]:
        return [
            Problem(ops=[
                Op("put", 1, 1, None),
                Op("put", 2, 2, None),
                Op("get", 1, None, 1),
                Op("get", 3, None, -1),
                Op("put", 2, 1, None),
                Op("get", 2, None, 1),
                Op("remove", 2, None, None),
                Op("get", 2, None, -1),
            ]),
            # Problem(ops=[...]),  # add your own
        ]

    @staticmethod
    def run(solver_class) -> List[Tuple[Problem, List[Tuple[Op, Optional[int], bool]], bool]]:
        all_results = []
        for prob in HashMap.get_test_cases():
            hm = solver_class()
            op_results = []
            all_passed = True
            for op in prob.ops:
                if op.kind == "put":
                    hm.put(op.key, op.value)
                    op_results.append((op, None, True))
                elif op.kind == "remove":
                    hm.remove(op.key)
                    op_results.append((op, None, True))
                else:
                    actual = hm.get(op.key)
                    passed = actual == op.expected
                    if not passed:
                        all_passed = False
                    op_results.append((op, actual, passed))
            all_results.append((prob, op_results, all_passed))
        return all_results
