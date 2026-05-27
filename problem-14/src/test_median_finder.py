"""Tests for MedianFinder. Outlines for optional tests, maybe useful after MedianFinder is functioning."""

import unittest
from stream import Problem
from solver import MedianFinder


class SolverTest(unittest.TestCase):

    def test_runs_without_error(self) -> None:
        for problem in Problem.get_test_cases():
            problem.run(MedianFinder())
        # Uncomment once MedianFinder is implemented:
        # for i, problem in enumerate(Problem.get_test_cases()):
        #     failures = [(op, a) for op, a, ok in problem.run(MedianFinder()) if not ok]
        #     self.assertEqual(failures, [], f"test {i+1} failures: {failures}")

    # def test_single_element(self) -> None:
    #     mf = MedianFinder()
    #     mf.addNum(1)
    #     self.assertAlmostEqual(mf.findMedian(), 1.0)

    # def test_two_elements(self) -> None:
    #     mf = MedianFinder()
    #     mf.addNum(1)
    #     mf.addNum(2)
    #     self.assertAlmostEqual(mf.findMedian(), 1.5)

    # def test_negative_numbers(self) -> None:
    #     mf = MedianFinder()
    #     for n in [-3, -1, -2]:
    #         mf.addNum(n)
    #     self.assertAlmostEqual(mf.findMedian(), -2.0)


if __name__ == "__main__":
    unittest.main()
