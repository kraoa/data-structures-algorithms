"""You'll implement this."""


class Solver:
    """
    Time: O(m * log(m*n)), Space: O(1).
    Binary search on the answer v in [1, m*n]. For a candidate v, count how
    many table entries are <= v: for each row i in 1..m, row i contains
    min(v // i, n) values <= v. Find the smallest v where count(v) >= k.
    """

    def find_kth_number(self, m: int, n: int, k: int) -> int:
        return 0
