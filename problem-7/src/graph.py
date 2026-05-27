"""Read this first."""

from typing import List, Tuple


class Graph:
    """
    Directed prerequisite graph for courses labeled 0 to num_courses-1.
    An edge (course, prereq) means prereq must be completed before course.
    """

    def __init__(self, num_courses: int, prerequisites: List[Tuple[int, int]]):
        self.num_courses = num_courses
        self.prerequisites = prerequisites

    def prereqs_of(self, course: int) -> List[int]:
        """Returns all courses that must be completed before this one."""
        return [pre for c, pre in self.prerequisites if c == course]

    def is_valid_order(self, order: List[int]) -> bool:
        """
        Returns True iff order is a valid topological ordering:
          - Contains every course label (0 to num_courses-1) exactly once.
          - Every prerequisite appears before its dependent course.
        """
        if sorted(order) != list(range(self.num_courses)):
            return False
        pos = {course: i for i, course in enumerate(order)}
        return all(pos[pre] < pos[course] for course, pre in self.prerequisites)

    def has_cycle(self) -> bool:
        """Returns True if the prerequisite graph contains a directed cycle."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * self.num_courses
        adj: List[List[int]] = [[] for _ in range(self.num_courses)]
        for course, pre in self.prerequisites:
            adj[course].append(pre)

        def dfs(node: int) -> bool:
            color[node] = GRAY
            for nb in adj[node]:
                if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                    return True
            color[node] = BLACK
            return False

        return any(color[i] == WHITE and dfs(i) for i in range(self.num_courses))


class Problem:
    """
    Given num_courses courses (labeled 0 to num_courses-1) and prerequisite
    pairs, return any valid ordering to complete all courses.
    Return [] if a cycle makes it impossible.
    """

    def __init__(self, graphs: List[Graph]):
        self.graphs = graphs

    def run(self, solver) -> List[Tuple[Graph, List[int], bool]]:
        """
        Calls solver.find_order(num_courses, prerequisites) for each graph.
        solver must expose .find_order(n: int, prereqs: List[Tuple[int,int]])
                                      -> List[int].
        An empty returned list is valid only when the graph contains a cycle.
        Returns (graph, returned_order, passed).
        """
        results = []
        for graph in self.graphs:
            order = solver.find_order(graph.num_courses, graph.prerequisites)
            if order == []:
                passed = graph.has_cycle()
            else:
                passed = graph.is_valid_order(order)
            results.append((graph, order, passed))
        return results

    @staticmethod
    def get_test_cases() -> List[Graph]:
        return [
            Graph(2, [(1, 0)]),                          # simple chain: 0 → 1
            Graph(4, [(1, 0), (2, 0), (3, 1), (3, 2)]),  # diamond
            Graph(2, [(1, 0), (0, 1)]),                   # cycle → []
            Graph(1, []),                                  # single course
            Graph(3, []),                                  # no prereqs — any order valid
            # Graph(?, [...]),                             # add your own
        ]
