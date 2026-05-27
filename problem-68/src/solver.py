"""You'll implement this."""

from typing import List


class Solver:
    """
    Time: O(n * 2^n), Space: O(n * 2^n).
    Represent visited nodes as a bitmask; state = (current_node, visited_mask).
    Seed the BFS queue with all (i, 1<<i, 0) simultaneously (start anywhere).
    Expand neighbors, updating the mask; return the step count the first time
    any state reaches the full mask (1<<n) - 1.
    """

    def shortest_path_length(self, graph: List[List[int]]) -> int:
        return 0
