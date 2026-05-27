"""Tests for the HashMap driver (must pass out of the box)."""

import unittest
from hashmap import HashMap, Op


class _ReferenceMap:
    """Plain Python dict wrapper for verifying expected values."""
    def __init__(self) -> None:
        self._d = {}

    def put(self, key: int, value: int) -> None:
        self._d[key] = value

    def get(self, key: int) -> int:
        return self._d.get(key, -1)

    def remove(self, key: int) -> None:
        self._d.pop(key, None)


class TestHashMap(unittest.TestCase):
    def test_expected_values_match_reference_dict(self) -> None:
        for prob in HashMap.get_test_cases():
            ref = _ReferenceMap()
            for op in prob.ops:
                if op.kind == "put":
                    ref.put(op.key, op.value)
                elif op.kind == "remove":
                    ref.remove(op.key)
                else:
                    expected_from_ref = ref.get(op.key)
                    self.assertEqual(op.expected, expected_from_ref,
                                     f"get({op.key}): expected {op.expected} but ref says {expected_from_ref}")

    def test_get_ops_have_int_expected(self) -> None:
        for prob in HashMap.get_test_cases():
            for op in prob.ops:
                if op.kind == "get":
                    self.assertIsInstance(op.expected, int)


if __name__ == "__main__":
    unittest.main()
