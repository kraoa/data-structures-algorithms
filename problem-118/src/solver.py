"""You'll implement this."""

from typing import List


class BloomFilter:
    """
    Time: O(num_hashes) per add/might_contain. Space: O(size) bits.
    Allocate a bit array of `size` bits, all zero. For add(item), compute
    hash((item, seed)) % size for seed in range(num_hashes) and set those bits.
    For might_contain(item), check the same bit positions — return False if any
    bit is 0 (definitive miss), True otherwise (probable hit, may be false positive).
    """

    def __init__(self, size: int, num_hashes: int) -> None:
        pass

    def add(self, item: str) -> None:
        pass

    def might_contain(self, item: str) -> bool:
        return False
