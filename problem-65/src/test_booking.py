"""Tests for the Problem driver (booking.py)."""

import unittest
from booking import Problem


class TestBooking(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for problem in Problem.get_test_cases():
            expected_seq = [op.expected for op in problem.ops]
            actual_seq = Problem.reference_sequence(problem.ops)
            self.assertEqual(
                expected_seq,
                actual_seq,
                msg=f"ops={problem.ops}",
            )

    def test_single_booking_is_one(self) -> None:
        self.assertEqual(Problem.brute_force_max_k([(10, 20)]), 1)

    def test_two_overlapping_bookings(self) -> None:
        self.assertEqual(Problem.brute_force_max_k([(10, 30), (20, 40)]), 2)

    def test_non_overlapping_is_one(self) -> None:
        self.assertEqual(Problem.brute_force_max_k([(10, 20), (30, 40)]), 1)


if __name__ == "__main__":
    unittest.main()
