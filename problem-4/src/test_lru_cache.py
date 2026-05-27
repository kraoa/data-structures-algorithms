"""Tests for LRUCache. Outlines for optional tests, maybe useful after LRUCache is functioning."""

import unittest
from operations import Problem
from solver import LRUCache


class SolverTest(unittest.TestCase):

    def test_basic_eviction(self) -> None:
        """LRU eviction with capacity 2 (LeetCode example)."""
        problem = Problem.get_test_cases()[0]
        cache = LRUCache(problem.capacity)
        problem.run(cache)
        # Uncomment once LRUCache is implemented:
        # failures = [(op, actual) for op, actual, passed in problem.run(cache) if not passed]
        # self.assertEqual(failures, [], f"failing ops: {failures}")

    # def test_all_cases(self) -> None:
    #     for i, problem in enumerate(Problem.get_test_cases()):
    #         cache = LRUCache(problem.capacity)
    #         failures = [(op, actual) for op, actual, passed in problem.run(cache) if not passed]
    #         self.assertEqual(failures, [], f"test {i + 1} failures: {failures}")

    # def test_overwrite_does_not_grow_cache(self) -> None:
    #     """Updating an existing key should not count as a new entry."""
    #     cache = LRUCache(2)
    #     cache.put(1, 1)
    #     cache.put(1, 10)  # update — still only 1 unique key
    #     cache.put(2, 2)   # should NOT evict anything
    #     self.assertEqual(cache.get(1), 10)
    #     self.assertEqual(cache.get(2), 2)

    # def test_get_updates_recency(self) -> None:
    #     """Accessing a key should protect it from eviction."""
    #     cache = LRUCache(2)
    #     cache.put(1, 1)
    #     cache.put(2, 2)
    #     cache.get(1)      # 1 is now most-recent; 2 becomes LRU
    #     cache.put(3, 3)   # evicts 2
    #     self.assertEqual(cache.get(2), -1)
    #     self.assertEqual(cache.get(1), 1)
    #     self.assertEqual(cache.get(3), 3)


if __name__ == "__main__":
    unittest.main()
