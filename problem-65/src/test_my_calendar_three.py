"""Tests for the Solver (MyCalendarThree)."""

import unittest
from solver import MyCalendarThree


class TestMyCalendarThree(unittest.TestCase):
    def test_no_crash_on_stub(self) -> None:
        cal = MyCalendarThree()
        cal.book(10, 20)
        cal.book(50, 60)

    # def test_leetcode_example(self) -> None:
    #     cal = MyCalendarThree()
    #     self.assertEqual(cal.book(10, 20), 1)
    #     self.assertEqual(cal.book(50, 60), 1)
    #     self.assertEqual(cal.book(10, 40), 2)
    #     self.assertEqual(cal.book(5, 15), 3)
    #     self.assertEqual(cal.book(5, 10), 3)
    #     self.assertEqual(cal.book(25, 55), 3)

    # def test_non_overlapping_stays_one(self) -> None:
    #     cal = MyCalendarThree()
    #     self.assertEqual(cal.book(1, 2), 1)
    #     self.assertEqual(cal.book(3, 4), 1)
    #     self.assertEqual(cal.book(5, 6), 1)

    # def test_all_same_interval(self) -> None:
    #     cal = MyCalendarThree()
    #     cal.book(5, 10)
    #     cal.book(5, 10)
    #     self.assertEqual(cal.book(5, 10), 3)


if __name__ == "__main__":
    unittest.main()
