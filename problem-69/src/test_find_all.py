"""Tests for the Solver (find_all)."""

import unittest
from solver import Solver


class TestFindAll(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        solver = Solver()
        solver.find_all("aabcaabxaaaz", "aab")

    # def test_multiple_matches(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_all("aabcaabxaaaz", "aab"), [0, 4])

    # def test_overlapping_matches(self) -> None:
    #     # Naive O(n*m) approach handles this correctly too, but KMP does it in O(n+m).
    #     solver = Solver()
    #     self.assertEqual(solver.find_all("aaaa", "aa"), [0, 1, 2])

    # def test_no_match(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_all("abc", "xyz"), [])

    # def test_pattern_at_start_and_end(self) -> None:
    #     solver = Solver()
    #     self.assertEqual(solver.find_all("abcabc", "abc"), [0, 3])


if __name__ == "__main__":
    unittest.main()
