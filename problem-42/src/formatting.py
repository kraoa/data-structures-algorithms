"""Read this first."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TestCase:
    words: List[str]
    max_width: int
    expected: List[str]


class Problem:
    """
    Format text so that each line is exactly max_width characters wide.

    Rules:
    - Pack as many words as possible per line (greedy).
    - Distribute spaces between words as evenly as possible. If spaces don't
      divide evenly, the leftmost gaps get more spaces.
    - The last line is left-justified (words separated by single spaces,
      padded with trailing spaces to max_width).
    - A line with a single word is left-justified.

    Example: words=["This","is","an","example","of","text","justification."],
             max_width=16
    → ["This    is    an",
       "example  of text",
       "justification.  "]
    """

    def __init__(self, test_cases: List[TestCase]):
        self.test_cases = test_cases

    @staticmethod
    def build_line(words: List[str], max_width: int, is_last: bool) -> str:
        """
        Format a single line from a group of words.
        Handles even/uneven space distribution and last-line special case.
        """
        if is_last or len(words) == 1:
            line = " ".join(words)
            return line + " " * (max_width - len(line))
        total_chars = sum(len(w) for w in words)
        total_spaces = max_width - total_chars
        gaps = len(words) - 1
        space_per_gap, extra = divmod(total_spaces, gaps)
        result = []
        for i, word in enumerate(words[:-1]):
            result.append(word)
            result.append(" " * (space_per_gap + (1 if i < extra else 0)))
        result.append(words[-1])
        return "".join(result)

    def run(self, solver) -> List[Tuple[TestCase, List[str], bool]]:
        """
        Calls solver.full_justify(words, max_width) for each test case.
        solver must expose .full_justify(words: List[str], max_width: int) -> List[str].
        Returns (test_case, actual, passed).
        """
        results = []
        for tc in self.test_cases:
            actual = solver.full_justify(list(tc.words), tc.max_width)
            results.append((tc, actual, actual == tc.expected))
        return results

    @staticmethod
    def get_test_cases() -> List[TestCase]:
        return [
            TestCase(
                ["This", "is", "an", "example", "of", "text", "justification."],
                16,
                ["This    is    an", "example  of text", "justification.  "],
            ),
            TestCase(
                ["What", "must", "be", "acknowledgment", "shall", "be"],
                16,
                ["What   must   be", "acknowledgment  ", "shall be        "],
            ),
            TestCase(
                ["Science", "is", "what", "we", "understand", "well", "enough",
                 "to", "explain", "to", "a", "computer.", "Art", "is",
                 "everything", "else", "we", "do"],
                20,
                ["Science  is  what we",
                 "understand      well",
                 "enough to explain to",
                 "a  computer.  Art is",
                 "everything  else  we",
                 "do                  "],
            ),
            # TestCase([???], ??, [???]),  # add your own
        ]
