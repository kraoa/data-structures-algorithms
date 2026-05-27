"""Tests for the Problem driver (lfu_ops.py)."""

import unittest
from cache_ops import Problem


class TestLfuOps(unittest.TestCase):
    def test_expected_values_match_naive(self) -> None:
        for problem in Problem.get_test_cases():
            results = Problem.naive_run(problem)
            for op, actual, passed in results:
                self.assertTrue(
                    passed,
                    msg=f"get({op.key}): got {actual}, expected {op.expected}",
                )

    def test_naive_evicts_lfu_on_put(self) -> None:
        from cache_ops import _NaiveLFU
        lfu = _NaiveLFU(2)
        lfu.put(1, 1)
        lfu.put(2, 2)
        lfu.get(1)          # freq(1)=2, freq(2)=1
        lfu.put(3, 3)       # evict key 2 (LFU)
        self.assertEqual(lfu.get(2), -1)
        self.assertEqual(lfu.get(1), 1)
        self.assertEqual(lfu.get(3), 3)

    def test_naive_capacity_zero(self) -> None:
        from cache_ops import _NaiveLFU
        lfu = _NaiveLFU(0)
        lfu.put(1, 1)
        self.assertEqual(lfu.get(1), -1)

    def test_naive_lru_tiebreak(self) -> None:
        from cache_ops import _NaiveLFU
        lfu = _NaiveLFU(2)
        lfu.put(1, 1)
        lfu.put(2, 2)
        # Both have freq=1; key 1 is LRU.
        lfu.put(3, 3)
        self.assertEqual(lfu.get(1), -1)   # evicted
        self.assertEqual(lfu.get(2), 2)
        self.assertEqual(lfu.get(3), 3)


if __name__ == "__main__":
    unittest.main()
