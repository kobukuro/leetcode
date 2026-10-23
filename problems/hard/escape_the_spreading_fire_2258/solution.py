# Tags: Array, Binary Search, Breadth-First Search, Matrix


class Solution:
    def maximum_minutes(self, grid: list[list[int]]) -> int:
        """
        Find the maximum number of minutes you can stay at the start cell and
        still reach the safehouse before the spreading fire catches you.

        Args:
            grid: An m x n matrix where 0 is grass, 1 is fire and 2 is a wall.
                  You start at (0, 0) and the safehouse is at (m - 1, n - 1).

        Returns:
            The maximum number of minutes you can wait, -1 if escaping is
            impossible even without waiting, or 10^9 if you can always escape
            no matter how long you wait.

        Time Complexity: O(m * n * log(L)), where L = 10^9
        - A multi-source BFS computes the fire's arrival time at every cell: O(m * n)
        - Each can_escape call runs one BFS for the person: O(m * n)
        - Binary search over the wait time in [0, L] makes O(log L) ≈ 30 calls

        Space Complexity: O(m * n)
        - The fire matrix stores the fire's arrival time at every cell
        - The fire BFS queue holds O(m * n) cells: each cell is enqueued at most
          once, and the initial queue already contains every fire cell
        - Each can_escape call allocates an m x n seen matrix, and its BFS queue
          also holds O(m * n) cells since every cell is enqueued at most once
        """
        m, n = len(grid), len(grid[0])
        INF = float("inf")
        LIMIT = 10 ** 9
        fire = [[INF] * n for _ in range(m)]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire[i][j] = 0
                    q.append((i, j))
        t = 0
        while q:
            t += 1
            nxt = []
            for x, y in q:
                for dx, dy in dirs:
                    a, b = x + dx, y + dy
                    if (
                            0 <= a < m
                            and 0 <= b < n
                            and fire[a][b] == INF
                            and grid[a][b] != 2
                    ):
                        fire[a][b] = t
                        nxt.append((a, b))
            q = nxt

        def can_escape(wait):
            if fire[0][0] <= wait:
                return False
            seen = [[False] * n for _ in range(m)]
            seen[0][0] = True
            t = wait
            q = [(0, 0)]
            while q:
                t += 1
                nxt = []
                for x, y in q:
                    for dx, dy in dirs:
                        a, b = x + dx, y + dy
                        if a < 0 or a == m or b < 0 or b == n or grid[a][b] == 2 or seen[a][b]:
                            continue
                        if a == m - 1 and b == n - 1:
                            if fire[a][b] >= t:
                                return True
                            continue
                        if fire[a][b] > t:
                            seen[a][b] = True
                            nxt.append((a, b))
                q = nxt
            return False

        if not can_escape(0):
            return -1
        if can_escape(LIMIT):
            return LIMIT
        l, h = 0, LIMIT
        while h - l > 1:
            mid = (l + h) // 2
            if can_escape(mid):
                l = mid
            else:
                h = mid
        return l
