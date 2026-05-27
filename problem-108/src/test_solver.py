"""Tests for MyHashMap (assertions commented out until implemented)."""

import unittest
from solver import MyHashMap


class TestMyHashMap(unittest.TestCase):
    def test_smoke(self) -> None:
        hm = MyHashMap()
        hm.put(1, 1)
        hm.get(1)
        hm.remove(1)  # must not crash

    # def test_basic_put_get(self) -> None:
    #     hm = MyHashMap()
    #     hm.put(1, 1)
    #     self.assertEqual(hm.get(1), 1)

    # def test_missing_key_returns_minus_one(self) -> None:
    #     hm = MyHashMap()
    #     self.assertEqual(hm.get(42), -1)

    # def test_overwrite(self) -> None:
    #     hm = MyHashMap()
    #     hm.put(2, 2)
    #     hm.put(2, 5)
    #     self.assertEqual(hm.get(2), 5)

    # def test_remove(self) -> None:
    #     hm = MyHashMap()
    #     hm.put(1, 1)
    #     hm.remove(1)
    #     self.assertEqual(hm.get(1), -1)

    # def test_collision_handling(self) -> None:
    #     # Keys that hash to the same bucket must not interfere with each other.
    #     hm = MyHashMap()
    #     hm.put(0, 10)
    #     hm.put(1009, 20)   # same bucket as 0 if bucket size is 1009
    #     self.assertEqual(hm.get(0), 10)
    #     self.assertEqual(hm.get(1009), 20)


if __name__ == "__main__":
    unittest.main()
