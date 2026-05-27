"""Tests for Solution (assertions commented out until implemented)."""

import unittest
from reservoir import build_list
from solver import Solution


class TestSolution(unittest.TestCase):
    def test_smoke(self) -> None:
        head = build_list([1, 2, 3])
        sol = Solution(head)
        sol.get_random()  # must not crash

    # def test_single_element_always_returned(self) -> None:
    #     head = build_list([42])
    #     sol = Solution(head)
    #     for _ in range(20):
    #         self.assertEqual(sol.get_random(), 42)

    # def test_all_values_appear(self) -> None:
    #     # With 300 trials and 3 values, all should appear at least once.
    #     head = build_list([1, 2, 3])
    #     sol = Solution(head)
    #     results = {sol.get_random() for _ in range(300)}
    #     self.assertEqual(results, {1, 2, 3})

    # def test_results_in_value_set(self) -> None:
    #     head = build_list([5, 10, 15])
    #     sol = Solution(head)
    #     for _ in range(50):
    #         self.assertIn(sol.get_random(), {5, 10, 15})


if __name__ == "__main__":
    unittest.main()
