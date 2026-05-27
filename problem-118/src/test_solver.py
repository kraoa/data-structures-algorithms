"""Tests for BloomFilter solver. Assertions are commented out until implemented."""

import unittest
from bloom_filter import Problem, Op
from solver import BloomFilter


class TestBloomFilterSolver(unittest.TestCase):
    def test_smoke(self) -> None:
        """Runs solver on all problems without asserting — stub must not crash."""
        for problem in Problem.get_test_cases():
            problem.run(BloomFilter)

    # def test_no_false_negatives(self) -> None:
    #     """Items that were added must always return True."""
    #     bf = BloomFilter(1000, 3)
    #     for item in ["hello", "world", "foo"]:
    #         bf.add(item)
    #     for item in ["hello", "world", "foo"]:
    #         self.assertTrue(bf.might_contain(item), f"False negative for {item!r}")

    # def test_empty_filter(self) -> None:
    #     bf = BloomFilter(100, 2)
    #     # An empty filter should return False for anything.
    #     self.assertFalse(bf.might_contain("anything"))

    # def test_false_positive_rate_reasonable(self) -> None:
    #     # With size=1000 and 3 hashes, false positive rate should be low for 10 items.
    #     import random, string
    #     random.seed(42)
    #     bf = BloomFilter(1000, 3)
    #     added = {f"item{i}" for i in range(10)}
    #     for item in added:
    #         bf.add(item)
    #     not_added = [
    #         "".join(random.choices(string.ascii_lowercase, k=8)) for _ in range(100)
    #         if "".join(random.choices(string.ascii_lowercase, k=8)) not in added
    #     ]
    #     false_positives = sum(1 for item in not_added if bf.might_contain(item))
    #     self.assertLess(false_positives / len(not_added), 0.10)


if __name__ == "__main__":
    unittest.main()
