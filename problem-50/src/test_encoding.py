"""Tests for Problem. Verifies stored expected values via a recursive decoder."""

import unittest
from encoding import Problem


class ProblemTest(unittest.TestCase):

    @staticmethod
    def _recursive_decode(s: str) -> str:
        """Recursive decoder: scan for outermost k[...] blocks."""
        result = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                k = 0
                while s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                # s[i] == '['
                depth, j = 1, i + 1
                while depth > 0:
                    if s[j] == "[":
                        depth += 1
                    elif s[j] == "]":
                        depth -= 1
                    j += 1
                inner = ProblemTest._recursive_decode(s[i + 1:j - 1])
                result.append(inner * k)
                i = j
            else:
                result.append(s[i])
                i += 1
        return "".join(result)

    def test_expected_values_match_recursive_decode(self) -> None:
        for tc in Problem.get_test_cases():
            ref = self._recursive_decode(tc.s)
            self.assertEqual(
                tc.expected, ref,
                f"s={tc.s!r}: stored={tc.expected!r}, recursive={ref!r}",
            )

    def test_recursive_no_encoding(self) -> None:
        self.assertEqual(self._recursive_decode("abc"), "abc")

    def test_recursive_nested(self) -> None:
        self.assertEqual(self._recursive_decode("2[3[a]]"), "aaaaaa")


if __name__ == "__main__":
    unittest.main()
