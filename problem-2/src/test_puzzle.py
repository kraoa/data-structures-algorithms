"""Tests for Puzzle. All of this is just boilerplate to make test cases compact and understandable."""

import unittest
from typing import List

from puzzle import Puzzle, Feedback


class TestCase:
    """Represents a test case for the puzzle."""

    def __init__(self, secret: str, guess: List[int], exp_bulls: int, exp_cows: int):
        self.secret = secret
        self.guess = guess
        self.exp_bulls = exp_bulls
        self.exp_cows = exp_cows


class PuzzleTest(unittest.TestCase):
    """Unit tests for the Puzzle class."""

    def test_check(self) -> None:
        """Test the puzzle feedback logic."""
        # Test cases:   secret,  guess,           bulls, cows
        all_cases = [
            TestCase("1234", [1, 2, 3, 4], 4, 0),  # exact match
            TestCase("1234", [1, 2, 3, 5], 3, 0),  # one wrong, no cow
            TestCase("1234", [4, 3, 2, 1], 0, 4),  # all reversed
            TestCase("1234", [1, 3, 2, 4], 2, 2),  # two bulls, two cows
            TestCase("1122", [2, 2, 1, 1], 0, 4),  # all cows, repeated digits
            TestCase("1122", [1, 2, 1, 2], 2, 2),  # duplicates: mix of bulls/cows
            TestCase("1111", [1, 2, 2, 2], 1, 0),  # extra guessed colors don't score
            # TestCase("1234", [?, ?, ?, ?], ?, ?),  # add your own edge cases
        ]

        failures = []
        for tc in all_cases:
            puzzle = Puzzle(tc.secret)
            try:
                feedback = puzzle.guess(tc.guess)
                if feedback.bulls != tc.exp_bulls or feedback.cows != tc.exp_cows:
                    failures.append(
                        f"secret={tc.secret}, guess={tc.guess}: "
                        f"got bulls={feedback.bulls} cows={feedback.cows}, "
                        f"expected bulls={tc.exp_bulls} cows={tc.exp_cows}"
                    )
            except Exception as e:
                failures.append(f"secret={tc.secret}, guess={tc.guess}: raised {e}")

        if failures:
            self.fail(
                "\n=== TEST CASE FAILURES ===\n" + "\n".join(failures) + "\n=== END ==="
            )

    def test_invalid_guess(self) -> None:
        """Test that invalid guesses raise ValueError."""
        puzzle = Puzzle("1234")
        with self.assertRaises(ValueError):
            puzzle.guess([7, 1, 2, 3])  # digit out of range
        with self.assertRaises(ValueError):
            puzzle.guess([1, 2, 3])  # wrong length


if __name__ == "__main__":
    unittest.main()
