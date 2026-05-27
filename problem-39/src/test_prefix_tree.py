"""Tests for Trie. Assertions are commented out until Trie is implemented."""

import unittest
from words import Problem
from solver import Trie


class TrieTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        for problem in Problem.get_test_cases():
            problem.run(Trie)

    # def test_search_exact_match(self) -> None:
    #     t = Trie()
    #     t.insert("apple")
    #     self.assertTrue(t.search("apple"))

    # def test_search_prefix_not_a_word(self) -> None:
    #     t = Trie()
    #     t.insert("apple")
    #     self.assertFalse(t.search("app"))

    # def test_starts_with_prefix(self) -> None:
    #     t = Trie()
    #     t.insert("apple")
    #     self.assertTrue(t.starts_with("app"))

    # def test_prefix_becomes_word_after_insert(self) -> None:
    #     t = Trie()
    #     t.insert("apple")
    #     self.assertFalse(t.search("app"))
    #     t.insert("app")
    #     self.assertTrue(t.search("app"))


if __name__ == "__main__":
    unittest.main()
