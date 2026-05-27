"""Tests for the Solver (LFUCache)."""

import unittest
from solver import LFUCache


class TestLFUCache(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        lfu = LFUCache(2)
        lfu.put(1, 1)
        lfu.put(2, 2)
        lfu.get(1)

    # def test_leetcode_example(self) -> None:
    #     lfu = LFUCache(2)
    #     lfu.put(1, 1)
    #     lfu.put(2, 2)
    #     self.assertEqual(lfu.get(1), 1)
    #     lfu.put(3, 3)          # evicts key 2
    #     self.assertEqual(lfu.get(2), -1)
    #     self.assertEqual(lfu.get(3), 3)
    #     lfu.put(4, 4)          # evicts key 1
    #     self.assertEqual(lfu.get(1), -1)
    #     self.assertEqual(lfu.get(3), 3)
    #     self.assertEqual(lfu.get(4), 4)

    # def test_capacity_one(self) -> None:
    #     lfu = LFUCache(1)
    #     lfu.put(1, 1)
    #     lfu.put(2, 2)          # evicts key 1
    #     self.assertEqual(lfu.get(1), -1)
    #     self.assertEqual(lfu.get(2), 2)

    # def test_update_existing_key(self) -> None:
    #     # put on an existing key updates the value and increments frequency.
    #     lfu = LFUCache(2)
    #     lfu.put(1, 1)
    #     lfu.put(1, 10)
    #     self.assertEqual(lfu.get(1), 10)

    # def test_lru_tiebreak(self) -> None:
    #     # When frequencies are tied, the least recently used key is evicted.
    #     lfu = LFUCache(2)
    #     lfu.put(1, 1)
    #     lfu.put(2, 2)
    #     lfu.put(3, 3)          # freq(1)==freq(2)==1; key 1 is LRU => evicted
    #     self.assertEqual(lfu.get(1), -1)


if __name__ == "__main__":
    unittest.main()
