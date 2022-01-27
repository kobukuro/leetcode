# Depth-First Search, Breadth-First Search, Graph, Topological Sort
# TODO need to be improved
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        # print(pre_map)
        visited = set()
        res = []

        def dfs(crs):
            if crs in res:
                return
            if crs in visited:
                return []
            if pre_map[crs] == []:
                if crs not in res:
                    res.append(crs)
            visited.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) == []:
                    return []
            visited.remove(crs)
            pre_map[crs] = []
            if crs not in res:
                res.append(crs)

        for i in range(numCourses):
            if dfs(i) == []:
                return []

        return res


if __name__ == '__main__':
    # numCourses = 3
    # prerequisites = [[1, 0], [1, 2], [0, 1]]
    numCourses = 6
    prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    print(Solution().findOrder(numCourses=numCourses, prerequisites=prerequisites))
