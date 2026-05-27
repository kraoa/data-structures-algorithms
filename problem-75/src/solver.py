"""You'll implement this."""

from typing import List


class Solver:
    """
    Time: O(log(n) * D) where D = len(digits), Space: O(log n).
    For lengths shorter than len(str(n)): contribute D^L for each length L.
    For length equal to len(str(n)): walk digit by digit — at each position
    count how many allowed digits are strictly less than the current digit of n,
    multiply by D^(remaining positions), then continue only if the current digit
    of n itself appears in the digit set.
    """

    def at_most_n_given_digit_set(self, digits: List[str], n: int) -> int:
        return 0
