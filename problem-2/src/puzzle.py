"""Read this first."""

from typing import List, Optional


class Feedback:
    """Result of a single guess: bulls are exact position matches, cows are right color wrong position."""

    def __init__(self, bulls: int, cows: int):
        self.bulls = bulls
        self.cows = cows

    def is_solved(self) -> bool:
        return self.bulls == Puzzle.CODE_LENGTH

    def __repr__(self) -> str:
        return f"Feedback(bulls={self.bulls}, cows={self.cows})"


class Puzzle:
    """
    Classic Mastermind: guess a secret code of CODE_LENGTH digits,
    each drawn from 1..NUM_COLORS (repetition allowed).

    Call guess() with a list of ints to get Feedback.
    Win by getting CODE_LENGTH bulls.
    """

    CODE_LENGTH = 4
    NUM_COLORS = 6  # valid digits are 1..NUM_COLORS

    def __init__(self, secret: Optional[str] = None):
        if secret is None:
            import random
            self._secret = [random.randint(1, self.NUM_COLORS) for _ in range(self.CODE_LENGTH)]
        else:
            self._secret = [int(c) for c in secret]
        self._guesses: List[List[int]] = []
        self._won = False

    def code_length(self) -> int:
        return self.CODE_LENGTH

    def num_colors(self) -> int:
        return self.NUM_COLORS

    def guess(self, code: List[int]) -> Feedback:
        if self._won:
            raise RuntimeError("already solved")
        if len(code) != self.CODE_LENGTH:
            raise ValueError(f"code must have exactly {self.CODE_LENGTH} digits")
        if not all(1 <= c <= self.NUM_COLORS for c in code):
            raise ValueError(f"each digit must be between 1 and {self.NUM_COLORS}")

        bulls = 0
        secret_remaining: List[int] = []
        guess_remaining: List[int] = []

        for i in range(self.CODE_LENGTH):
            if code[i] == self._secret[i]:
                bulls += 1
            else:
                secret_remaining.append(self._secret[i])
                guess_remaining.append(code[i])

        cows = 0
        for g in guess_remaining:
            if g in secret_remaining:
                cows += 1
                secret_remaining.remove(g)

        feedback = Feedback(bulls, cows)
        self._guesses.append(list(code))

        if feedback.is_solved():
            self._won = True

        return feedback

    def won(self) -> bool:
        return self._won

    def num_guesses(self) -> int:
        return len(self._guesses)

    def admit_defeat(self) -> str:
        return "".join(str(c) for c in self._secret)
