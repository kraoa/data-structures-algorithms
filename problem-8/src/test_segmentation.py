"""Tests for Problem. Verifies the segmentation validator."""

import unittest
from segmentation import Problem


class ProblemTest(unittest.TestCase):

    _DICT = {"cat", "cats", "and", "sand", "dog"}
    _S = "catsanddog"

    def _chk(self, result, expected):
        return Problem._check(self._S, self._DICT, result, expected)

    def test_correct_full_result_passes(self) -> None:
        result = ["cats and dog", "cat sand dog"]
        expected = ["cats and dog", "cat sand dog"]
        self.assertTrue(self._chk(result, expected))

    def test_order_insensitive(self) -> None:
        result = ["cat sand dog", "cats and dog"]
        expected = ["cats and dog", "cat sand dog"]
        self.assertTrue(self._chk(result, expected))

    def test_missing_sentence_fails(self) -> None:
        result = ["cats and dog"]          # "cat sand dog" is missing
        expected = ["cats and dog", "cat sand dog"]
        self.assertFalse(self._chk(result, expected))

    def test_extra_invalid_sentence_fails(self) -> None:
        result = ["cats and dog", "cat sand dog", "cats sand og"]
        expected = ["cats and dog", "cat sand dog"]
        self.assertFalse(self._chk(result, expected))  # "og" not in dict

    def test_word_not_in_dict_fails(self) -> None:
        result = ["catsand dog"]           # "catsand" not in dict
        self.assertFalse(self._chk(result, ["cats and dog", "cat sand dog"]))

    def test_wrong_concatenation_fails(self) -> None:
        result = ["cat sand"]              # joins to "catsand" ≠ s
        self.assertFalse(self._chk(result, ["cats and dog", "cat sand dog"]))

    def test_empty_both_empty(self) -> None:
        self.assertTrue(Problem._check("xyz", {"abc"}, [], []))

    def test_single_word_sentence(self) -> None:
        self.assertTrue(Problem._check("a", {"a"}, ["a"], ["a"]))


if __name__ == "__main__":
    unittest.main()
