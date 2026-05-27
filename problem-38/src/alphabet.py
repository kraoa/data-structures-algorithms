"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Set, Tuple


@dataclass
class TestCase:
    words: List[str]
    n_chars: int    # number of unique characters appearing in words
    possible: bool  # False when the word list implies a contradictory ordering


class Problem:
    """
    A list of words is sorted lexicographically according to an unknown alien
    alphabet. Derive a valid character ordering consistent with that sort.
    Return any one valid ordering as a string containing all unique characters.
    Return "" if the ordering is impossible (e.g. a longer word is a prefix of
    a shorter word that comes after it, or the constraints form a cycle).

    Example: words = ["wrt","wrf","er","ett","rftt"] → "wertf" (one valid order)
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def extract_constraints(words: List[str]) -> Optional[List[Tuple[str, str]]]:
        """
        Scan adjacent word pairs for the first differing character.
        Returns a list of (before, after) pairs, or None if the list is
        immediately invalid (a word is a proper prefix of its predecessor).
        """
        constraints: List[Tuple[str, str]] = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    constraints.append((c1, c2))
                    break
            else:
                if len(w1) > len(w2):
                    return None  # prefix violation
        return constraints

    @staticmethod
    def is_valid_order(order: str, words: List[str]) -> bool:
        """Return True if `order` is consistent with every adjacent word pair."""
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if rank.get(c1, -1) >= rank.get(c2, -1):
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True

    def run(self, solver) -> List[Tuple[TestCase, str, bool]]:
        """
        Calls solver.alien_order(words) for each test case.
        solver must expose .alien_order(words: List[str]) -> str.
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.alien_order(list(tc.words))
            if not tc.possible:
                passed = actual == ""
            else:
                passed = (
                    len(actual) == tc.n_chars
                    and Problem.is_valid_order(actual, tc.words)
                )
            results.append((tc, actual, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(["z", "x"],                              2, True),
            TestCase(["wrt", "wrf", "er", "ett", "rftt"],     5, True),
            TestCase(["z", "x", "z"],                         2, False),  # cycle
            TestCase(["abc", "ab"],                           3, False),  # prefix violation
            TestCase(["a", "b", "ca", "cb"],                  3, True),
            TestCase(["aa", "bb"],                            2, True),
            # TestCase(["???"], ??, ???),  # add your own
        ]
