"""Tests for the bloom_filter driver. Must pass out of the box."""

import unittest
from bloom_filter import Problem, Op


class ReferenceBloomFilter:
    """Reference using a plain set — no false negatives, ignores false positives."""

    def __init__(self, size: int, num_hashes: int) -> None:
        self._added: set = set()

    def add(self, item: str) -> None:
        self._added.add(item)

    def might_contain(self, item: str) -> bool:
        # Set membership: definitively True for added items, False for others.
        return item in self._added


class TestBloomFilterDriver(unittest.TestCase):
    def test_no_false_negatives_with_reference(self) -> None:
        """Items that were added must always return True (no false negatives)."""
        for problem in Problem.get_test_cases():
            ref = ReferenceBloomFilter(problem.size, problem.num_hashes)
            for op in problem.ops:
                if op.kind == "add":
                    ref.add(op.item)
                elif op.expected is True:
                    result = ref.might_contain(op.item)
                    self.assertTrue(
                        result,
                        msg=f"might_contain({op.item!r}): reference returned False for an added item",
                    )

    def test_run_returns_correct_structure(self) -> None:
        for problem in Problem.get_test_cases():
            results = problem.run(ReferenceBloomFilter)
            self.assertEqual(len(results), len(problem.ops))

    def test_run_passes_for_definite_ops(self) -> None:
        """run() must pass for all ops where expected is not None."""
        for problem in Problem.get_test_cases():
            results = problem.run(ReferenceBloomFilter)
            for op, actual, passed in results:
                if op.expected is not None:
                    self.assertTrue(
                        passed,
                        msg=f"Reference failed definite op={op}, actual={actual}",
                    )


if __name__ == "__main__":
    unittest.main()
