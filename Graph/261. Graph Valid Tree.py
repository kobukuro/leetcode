# Depth-First Search, Breadth-First Search, Union Find, Graph
from collections import defaultdict
from typing import List


# Let E be the number of edges, and N be the number of nodes.
# Time Complexity : O(N+E).
# Creating the adjacency list requires initialising a list of length N,
# with a cost of O(N), and then iterating over and inserting E edges,
# for a cost of O(E). This gives us O(E) + O(N) = O(N+E).
# Each node is added to the stack once.
# For each of the N nodes, its adjacent edges is iterated over once.
# In total, this means that all E edges are iterated over once by the loop.
# This, therefore, gives a total time complexity of O(N+E).
# Because both parts are the same, we get a final time complexity of O(N+E).
#
# Space Complexity : O(N+E).
# The adjacency list is a list of length N, with inner lists with lengths that add to a total of E.
# This gives a total of O(N+E) space.
# In the worst case, the stack will have all N nodes on it at the same time,
# giving a total of O(N) space.
# In total, this gives us O(N+E) space.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
