"""Tests for Problem. Verifies build_line helper and stored expected values."""

import unittest
from formatting import Problem


class ProblemTest(unittest.TestCase):

    def test_build_line_even_spaces(self) -> None:
        line = Problem.build_line(["a", "b", "c"], 9, is_last=False)
        self.assertEqual(len(line), 9)
        self.assertEqual(line, "a   b   c")

    def test_build_line_uneven_spaces(self) -> None:
        # 3 words, 10 chars wide: 1 extra space goes to the first gap.
        line = Problem.build_line(["ab", "cd", "ef"], 10, is_last=False)
        self.assertEqual(len(line), 10)
        self.assertTrue(line.startswith("ab"))

    def test_build_line_last_line(self) -> None:
        line = Problem.build_line(["hello", "world"], 12, is_last=True)
        self.assertEqual(len(line), 12)
        self.assertEqual(line, "hello world ")

    def test_build_line_single_word(self) -> None:
        line = Problem.build_line(["word"], 10, is_last=False)
        self.assertEqual(len(line), 10)
        self.assertEqual(line, "word      ")

    def test_all_lines_have_correct_width(self) -> None:
        for tc in Problem.get_test_cases():
            for line in tc.expected:
                self.assertEqual(
                    len(line), tc.max_width,
                    f"expected line {line!r} has width {len(line)}, want {tc.max_width}",
                )


if __name__ == "__main__":
    unittest.main()
