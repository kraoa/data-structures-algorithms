"""You'll implement this."""

import random


class SkipList:
    """
    Time: O(log n) expected per operation. Space: O(n log n) expected.
    Maintain a tower of sorted linked lists; the bottom level holds all elements.
    Each element is promoted to the next level with probability p=0.5. To
    insert, find the insertion point at each level using forward pointers, then
    link in the new node at each level it was promoted to. Search and delete
    follow the same top-down traversal.
    """

    def insert(self, val: int) -> None:
        pass

    def search(self, val: int) -> bool:
        return False

    def delete(self, val: int) -> None:
        pass
