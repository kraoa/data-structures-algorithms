"""Tests for Problem helpers. Verifies extract_constraints and is_valid_order."""

import unittest
from alphabet import Problem


class ProblemTest(unittest.TestCase):

    def test_extract_constraints_simple(self) -> None:
        constraints = Problem.extract_constraints(["z", "x"])
        self.assertEqual(constraints, [("z", "x")])

    def test_extract_constraints_multiple(self) -> None:
        constraints = Problem.extract_constraints(["wrt", "wrf", "er", "ett", "rftt"])
        self.assertIn(("t", "f"), constraints)
        self.assertIn(("w", "e"), constraints)
        self.assertIn(("r", "t"), constraints)
        self.assertIn(("e", "r"), constraints)

    def test_extract_constraints_prefix_violation(self) -> None:
        # "abc" before "ab": "ab" is a proper prefix of "abc" but listed after it.
        result = Problem.extract_constraints(["abc", "ab"])
        self.assertIsNone(result)

    def test_extract_constraints_prefix_valid(self) -> None:
        # "ab" before "abc" is fine — no constraint generated, just no edge.
        result = Problem.extract_constraints(["ab", "abc"])
        self.assertIsNotNone(result)

    def test_is_valid_order_correct(self) -> None:
        self.assertTrue(Problem.is_valid_order("zx", ["z", "x"]))

    def test_is_valid_order_wrong_direction(self) -> None:
        self.assertFalse(Problem.is_valid_order("xz", ["z", "x"]))

    def test_is_valid_order_prefix_violation(self) -> None:
        self.assertFalse(Problem.is_valid_order("abc", ["abc", "ab"]))


if __name__ == "__main__":
    unittest.main()
