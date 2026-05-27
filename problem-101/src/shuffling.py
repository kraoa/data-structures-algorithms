"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    kind: str            # "reset" or "shuffle"
    expected: Optional[List[int]]  # None for shuffle (non-deterministic)


@dataclass
class Problem:
    nums: List[int]
    ops: List[Op]


class Shuffling:
    @staticmethod
    def get_test_cases() -> List[Problem]:
        return [
            Problem(
                nums=[1, 2, 3],
                ops=[
                    Op("shuffle", None),
                    Op("shuffle", None),
                    Op("reset", [1, 2, 3]),
                    Op("shuffle", None),
                    Op("reset", [1, 2, 3]),
                ],
            ),
            Problem(
                nums=[1],
                ops=[
                    Op("shuffle", [1]),
                    Op("reset", [1]),
                ],
            ),
            # Problem(nums=???, ops=[...]),  # add your own
        ]

    @staticmethod
    def run(solver_class) -> List[Tuple[Problem, List[Tuple[Op, List[int], bool]], bool]]:
        all_results = []
        for prob in Shuffling.get_test_cases():
            solution = solver_class(list(prob.nums))
            op_results = []
            all_passed = True
            for op in prob.ops:
                if op.kind == "reset":
                    actual = solution.reset()
                    passed = actual == op.expected
                else:
                    actual = solution.shuffle()
                    passed = sorted(actual) == sorted(prob.nums)
                if not passed:
                    all_passed = False
                op_results.append((op, actual, passed))
            all_results.append((prob, op_results, all_passed))
        return all_results
