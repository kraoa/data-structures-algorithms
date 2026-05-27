"""You'll implement this."""

from typing import Dict, List


class FreqStack:
    """
    Time: O(1) per push and pop, Space: O(n).
    Maintain freq (val -> count), group (count -> stack of vals pushed at that
    count), and maxfreq. push: increment freq[val], append val to group[freq[val]],
    update maxfreq. pop: pop from group[maxfreq], decrement freq of that val,
    if group[maxfreq] is empty decrement maxfreq. Ties are broken by recency
    automatically because group[count] is a stack (LIFO).
    """

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        return -1
