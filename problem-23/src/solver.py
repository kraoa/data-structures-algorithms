"""You'll implement this."""

from typing import List


class Solver:
    """
    Time: O(n * L^2), Space: O(n * L) where n = len(words), L = max word length.
    Build a map of word -> index. For each word w at index i, try every split
    point k: if w[:k] is a palindrome and reverse(w[k:]) exists in the map,
    emit (map[rev], i); if w[k:] is a palindrome and reverse(w[:k]) exists in
    the map (and k != 0 to avoid duplicates), emit (i, map[rev]).
    """

    def palindrome_pairs(self, words: List[str]) -> List[List[int]]:
        return []
