"""Read this first."""

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Op:
    """A single trie operation."""
    kind: str              # "insert", "search", or "startswith"
    word: str
    expected: Optional[bool]  # None for "insert"; True/False for lookups

    def __repr__(self) -> str:
        if self.kind == "insert":
            return f"insert({self.word!r})"
        return f"{self.kind}({self.word!r}) -> {self.expected}"


class Problem:
    """
    Defines a sequence of trie operations with expected outputs.

    Call run() with your Trie class to replay the operations and get
    (op, actual, passed) tuples for every search/startswith call.
    """

    def __init__(self, ops: List[Op]):
        self.ops = ops

    def run(self, trie_class) -> List[Tuple[Op, Optional[bool], bool]]:
        """
        Instantiates trie_class(), then replays all ops.
        trie_class must expose:
          .insert(word: str) -> None
          .search(word: str) -> bool
          .starts_with(prefix: str) -> bool
        Returns (op, actual, passed) for every non-insert op.
        """
        trie = trie_class()
        results = []
        for op in self.ops:
            if op.kind == "insert":
                trie.insert(op.word)
            elif op.kind == "search":
                actual = trie.search(op.word)
                results.append((op, actual, actual == op.expected))
            else:
                actual = trie.starts_with(op.word)
                results.append((op, actual, actual == op.expected))
        return results

    @staticmethod
    def get_test_cases() -> List["Problem"]:
        return [
            # LeetCode example
            Problem([
                Op("insert",     "apple",  None),
                Op("search",     "apple",  True),
                Op("search",     "app",    False),
                Op("startswith", "app",    True),
                Op("insert",     "app",    None),
                Op("search",     "app",    True),
            ]),
            # Prefix vs. exact match
            Problem([
                Op("insert",     "hello",  None),
                Op("insert",     "world",  None),
                Op("search",     "world",  True),
                Op("search",     "wor",    False),
                Op("startswith", "wor",    True),
                Op("startswith", "xyz",    False),
                Op("search",     "xyz",    False),
            ]),
            # Empty trie
            Problem([
                Op("search",     "a",      False),
                Op("startswith", "a",      False),
                Op("insert",     "a",      None),
                Op("search",     "a",      True),
            ]),
            # TestCase: add your own Problem([...]) here
        ]
