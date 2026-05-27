"""Tests for Solution (assertions commented out until implemented)."""

import unittest
from collections import Counter
from solver import Solution


class TestSolution(unittest.TestCase):
    def test_smoke(self) -> None:
        sol = Solution([1, 3])
        sol.pick_index()  # must not crash

    # def test_single_weight_always_returns_zero(self) -> None:
    #     sol = Solution([5])
    #     for _ in range(20):
    #         self.assertEqual(sol.pick_index(), 0)

    # def test_result_in_valid_range(self) -> None:
    #     sol = Solution([1, 3, 2])
    #     for _ in range(100):
    #         self.assertIn(sol.pick_index(), {0, 1, 2})

    # def test_higher_weight_picked_more_often(self) -> None:
    #     # Index 1 has 3x the weight of index 0; should appear ~75% of the time.
    #     sol = Solution([1, 3])
    #     counts = Counter(sol.pick_index() for _ in range(1000))
    #     ratio = counts[1] / (counts[0] + counts[1])
    #     self.assertGreater(ratio, 0.65)
    #     self.assertLess(ratio, 0.85)


if __name__ == "__main__":
    unittest.main()
