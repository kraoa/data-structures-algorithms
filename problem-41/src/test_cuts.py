"""Tests for Problem. Verifies stored expected values via a brute-force partitioner."""

import unittest
from typing import List, Tuple

from cuts import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _is_palindrome(t: str) -> bool:
        return t == t[::-1]

    @staticmethod
    def _brute_force(s: str) -> List[List[str]]:
        """Generate all 2^(n-1) cut positions; keep those where every part is a palindrome."""
        n = len(s)
        result = []
        for mask in range(1 << (n - 1)):
            parts = []
            start = 0
            for bit in range(n - 1):
                if mask >> bit & 1:
                    parts.append(s[start:bit + 1])
                    start = bit + 1
            parts.append(s[start:])
            if all(ProblemTest._is_palindrome(p) for p in parts):
                result.append(parts)
        return result

    @staticmethod
    def _normalize(partitions: List[List[str]]) -> List[Tuple[str, ...]]:
        return sorted(tuple(p) for p in partitions)

    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._brute_force(tc.s)
            self.assertEqual(
                self._normalize(tc.expected),
                self._normalize(ref),
                f"s={tc.s!r}: stored={tc.expected}, brute={ref}",
            )

    def test_brute_force_single_char(self) -> None:
        self.assertEqual(self._brute_force("a"), [["a"]])

    def test_brute_force_no_palindrome_partition_missed(self) -> None:
        result = self._brute_force("aab")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
