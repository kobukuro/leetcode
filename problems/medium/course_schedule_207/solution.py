# Tags: DFS, Graph
from typing import List


class Solution:
    # V:# of courses, E:# of dependencies
    # Time complexity: O(V+E)
    # Space complexity: O(V+E)
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(num_courses)}
        for pair in prerequisites:
            pre_map[pair[0]].append(pair[1])
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not pre_map[crs]:
                return True
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                pre_map[crs].remove(pre)
            visited.remove(crs)
            return True

        for c in range(num_courses):
            if not dfs(c):
                return False
        return True
