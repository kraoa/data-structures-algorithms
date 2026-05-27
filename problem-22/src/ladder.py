"""Read this first."""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class TestCase:
    begin_word: str
    end_word: str
    word_list: List[str]
    expected: int  # length of shortest transformation sequence, 0 if impossible


class Problem:
    """
    Transform begin_word into end_word one letter at a time. Each
    intermediate word must appear in word_list. Return the number of
    words in the shortest transformation sequence (including begin and
    end), or 0 if no such sequence exists.

    Example: "hit" → "cog", wordList=["hot","dot","dog","lot","log","cog"] → 5
             hit→hot→dot→dog→cog
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    def run(self, solver) -> List[Tuple[TestCase, int, bool]]:
        results = []
        for tc in self.test_cases:
            actual = solver.ladder_length(tc.begin_word, tc.end_word, list(tc.word_list))
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            TestCase("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),  # cog not in list
            TestCase("a", "c", ["a", "b", "c"], 2),
            TestCase("hot", "dog", ["hot", "dog"], 0),   # differ by 2 letters
            TestCase("abc", "abc", ["abc"], 1),           # begin == end
            # TestCase("???", "???", [...], ?),            # add your own
        ]
