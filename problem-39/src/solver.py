"""You'll implement this."""


class Trie:
    """
    Target: O(m) per operation where m = word/prefix length; O(total_chars) space.
    Each node holds a dict mapping characters to child nodes and an is_end flag.
    insert: walk chars, creating nodes as needed; mark the last node as is_end.
    search: walk chars; return True only if the path exists AND is_end is set.
    starts_with: walk chars; return True as long as the path exists.
    """

    def __init__(self) -> None:
        pass

    def insert(self, word: str) -> None:
        return

    def search(self, word: str) -> bool:
        return False

    def starts_with(self, prefix: str) -> bool:
        return False
