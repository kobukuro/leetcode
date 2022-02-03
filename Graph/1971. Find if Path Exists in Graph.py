# Depth-First Search, Breadth-First Search, Graph
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # print(graph)
        visited = set()

        def dfs(curr):
            if curr == destination:
                return True
            for nei in graph[curr]:
                if (curr, nei) not in visited:
                    visited.add((curr, nei))
                    if dfs(nei):
                        return True
            return False

        return dfs(source)


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    print(Solution().validPath(n=n, edges=edges, source=source, destination=destination))
