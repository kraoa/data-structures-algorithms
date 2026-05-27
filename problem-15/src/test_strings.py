"""Tests for Problem. Verifies stored expected values via the classic O(mn) DP."""

import unittest
from strings import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _edit_distance_dp(word1: str, word2: str) -> int:
        """Standard O(mn) DP reference."""
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[:]
            dp[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev[j - 1]
                else:
                    dp[j] = 1 + min(prev[j], dp[j - 1], prev[j - 1])
        return dp[n]

    def test_expected_values_match_dp(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._edit_distance_dp(tc.word1, tc.word2)
            self.assertEqual(
                tc.expected, ref,
                f"({repr(tc.word1)}, {repr(tc.word2)}): stored={tc.expected}, dp={ref}",
            )

    def test_dp_empty_strings(self) -> None:
        self.assertEqual(self._edit_distance_dp("", ""), 0)
        self.assertEqual(self._edit_distance_dp("abc", ""), 3)
        self.assertEqual(self._edit_distance_dp("", "abc"), 3)

    def test_dp_identical(self) -> None:
        self.assertEqual(self._edit_distance_dp("abc", "abc"), 0)

    def test_dp_symmetric(self) -> None:
        # Edit distance is symmetric.
        self.assertEqual(
            self._edit_distance_dp("horse", "ros"),
            self._edit_distance_dp("ros", "horse"),
        )


if __name__ == "__main__":
    unittest.main()
