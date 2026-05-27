"""Tests for Solution (assertions commented out until implemented)."""

import unittest
from shuffling import Shuffling
from solver import Solution


class TestSolution(unittest.TestCase):
    def test_smoke(self) -> None:
        sol = Solution([1, 2, 3])
        sol.shuffle()
        sol.reset()  # must not crash

    # def test_reset_returns_original(self) -> None:
    #     sol = Solution([1, 2, 3])
    #     sol.shuffle()
    #     self.assertEqual(sol.reset(), [1, 2, 3])

    # def test_shuffle_is_permutation(self) -> None:
    #     sol = Solution([1, 2, 3])
    #     result = sol.shuffle()
    #     self.assertEqual(sorted(result), [1, 2, 3])

    # def test_reset_after_multiple_shuffles(self) -> None:
    #     sol = Solution([1, 2, 3])
    #     sol.shuffle()
    #     sol.shuffle()
    #     self.assertEqual(sol.reset(), [1, 2, 3])

    # def test_single_element(self) -> None:
    #     sol = Solution([1])
    #     self.assertEqual(sol.shuffle(), [1])
    #     self.assertEqual(sol.reset(), [1])


if __name__ == "__main__":
    unittest.main()
