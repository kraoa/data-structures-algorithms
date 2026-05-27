"""Tests for Problem. Verifies stored expected values via a naive set-based trie."""

import unittest
from words import Problem


class NaiveTrie:
    """Reference implementation backed by a plain Python set."""

    def __init__(self) -> None:
        self._words: set = set()

    def insert(self, word: str) -> None:
        self._words.add(word)

    def search(self, word: str) -> bool:
        return word in self._words

    def starts_with(self, prefix: str) -> bool:
        return any(w.startswith(prefix) for w in self._words)


class ProblemTest(unittest.TestCase):

    def test_expected_values_match_naive_trie(self) -> None:
        for i, problem in enumerate(Problem.get_test_cases()):
            results = problem.run(NaiveTrie)
            failures = [(op, actual) for op, actual, passed in results if not passed]
            self.assertEqual(
                failures, [],
                f"Test {i + 1}: naive trie disagrees on {failures}",
            )

    def test_naive_search_absent(self) -> None:
        t = NaiveTrie()
        self.assertFalse(t.search("missing"))

    def test_naive_prefix_vs_exact(self) -> None:
        t = NaiveTrie()
        t.insert("apple")
        self.assertFalse(t.search("app"))
        self.assertTrue(t.starts_with("app"))


if __name__ == "__main__":
    unittest.main()
