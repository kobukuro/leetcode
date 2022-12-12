# Depth-First Search, Breadth-First Search, Union Find, Graph
from collections import defaultdict
from typing import List


# Here E = Number of edges, V = Number of vertices.
# Time complexity:O(E+V).
# Building the adjacency map will take O(E) operations,
# as we iterate over the list of edges once, and insert each edge into two lists.
# During the DFS traversal, each vertex will only be visited once.
# This is because we mark each vertex as visited as soon as we see it,
# and then we only visit vertices that are not marked as visited.
# In addition, when we iterate over the edge list of each vertex,
# we look at each edge once. This has a total cost of O(E+V).

# Space complexity: O(E+V).
# Building the adjacency map will take O(E) space.
# To keep track of visited vertices, a hashset of size O(V) is required.
# Also, the run-time stack for DFS will use O(V) space.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash_map = defaultdict(list)
        for edge in edges:
            hash_map[edge[0]].append(edge[1])
            hash_map[edge[1]].append(edge[0])
        visited = set()
        res = 0

        def dfs(curr):
            if curr in visited:
                return False
            visited.add(curr)
            for end in hash_map[curr]:
                dfs(end)
            return True

        for i in range(n):
            if dfs(i):
                res += 1
        return res
