# Depth-First Search, Breadth-First Search, Graph, Topological Sort
# difficult for me
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # V:# of courses, E:# of dependencies
        # Time:O(V+E), Space:O(V+E)
        pre_map = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            pre_map[pair[0]].append(pair[1])
        # print(pre_map)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                else:
                    pre_map[crs].remove(pre)
            visited.remove(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


if __name__ == '__main__':
    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(Solution().canFinish(numCourses=numCourses, prerequisites=prerequisites))
