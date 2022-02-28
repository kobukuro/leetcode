# Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph, Bitmask
# reference:https://www.youtube.com/watch?v=fzFaqBpDXy8
# reference:https://www.cnblogs.com/grandyang/p/11410007.html

from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # n=4, final_status=1111 (2進制)
        # 1往左4位 -> 10000 -> -1 -> 1111
        final_status = (1 << n) - 1
        queue = deque()
        visited = set()
        # n=4, queue:[(0,0001),(1,0010),(2,0100),(3,1000)]
        # 由右至左, 只有第0個node走過, 就是0001, 走過為1
        for i in range(n):
            queue.append((i, (1 << i)))
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur_num, cur_status = queue.popleft()
                # print(cur_num, bin(cur_status))
                visited.add((cur_num, cur_status))
                if cur_status == final_status:
                    return steps
                for next_num in graph[cur_num]:
                    # OR運算, 只要有1就是1, 否則為0
                    next_status = cur_status | (1 << next_num)
                    if (next_num, next_status) not in visited:
                        visited.add((next_num, next_status))
                        queue.append((next_num, next_status))
            steps += 1
        return -1


if __name__ == '__main__':
    graph = [[1, 2, 3], [0], [0], [0]]
    print(Solution().shortestPathLength(graph=graph))
