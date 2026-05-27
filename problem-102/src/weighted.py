"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Problem:
    w: List[int]
    trials: int


class Weighted:
    @staticmethod
    def get_test_cases() -> List[Problem]:
        return [
            Problem(w=[1, 3], trials=400),
            Problem(w=[1], trials=10),
            # Problem(w=???, trials=???),  # add your own
        ]

    @staticmethod
    def run(solver_class) -> List[Tuple[Problem, List[int], bool]]:
        results = []
        for prob in Weighted.get_test_cases():
            solution = solver_class(list(prob.w))
            picks = [solution.pick_index() for _ in range(prob.trials)]
            passed = all(0 <= r < len(prob.w) for r in picks)
            results.append((prob, picks, passed))
        return results
