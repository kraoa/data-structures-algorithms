"""Tests for Serializer. Outlines for optional tests, maybe useful after Serializer is functioning."""

import unittest
from tree import Problem
from solver import Serializer


class SerializerTest(unittest.TestCase):

    def test_empty_tree(self) -> None:
        """serialize(None) → deserialize should return None."""
        serializer = Serializer()
        problem = Problem([])
        # Uncomment once Serializer is implemented:
        # self.assertTrue(problem.check(serializer), "failed on empty tree")

    def test_single_node(self) -> None:
        serializer = Serializer()
        problem = Problem([1])
        # Uncomment once Serializer is implemented:
        # self.assertTrue(problem.check(serializer), "failed on single node")

    # def test_all_cases(self) -> None:
    #     serializer = Serializer()
    #     for i, problem in enumerate(Problem.get_test_cases()):
    #         self.assertTrue(problem.check(serializer), f"test case {i + 1} failed")

    # def test_distinct_trees_distinct_encodings(self) -> None:
    #     """Different trees should produce different encoded strings."""
    #     from tree import from_list
    #     serializer = Serializer()
    #     enc_left  = serializer.serialize(from_list([1, 2]))      # 2 is left child
    #     enc_right = serializer.serialize(from_list([1, None, 2])) # 2 is right child
    #     self.assertNotEqual(enc_left, enc_right)


if __name__ == "__main__":
    unittest.main()
