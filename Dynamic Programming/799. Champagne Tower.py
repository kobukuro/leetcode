# Dynamic Programming
# reference:https://www.youtube.com/watch?v=OqXzKsEWM44
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for i in range(100):
            dp.append([0] * (i + 1))
        dp[0][0] = poured
        # print(dp)
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] > 1:
                    if i + 1 < len(dp):
                        dp[i + 1][j] += (dp[i][j] - 1) / 2
                        if j + 1 < len(dp[i + 1]):
                            dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
                        dp[i][j] = 1
        # print(dp)
        return dp[query_row][query_glass]


if __name__ == '__main__':
    poured = 100000009
    query_row = 33
    query_glass = 17
    print(Solution().champagneTower(poured=poured, query_row=query_row, query_glass=query_glass))
    # 1 -> [[1]]
    # 2 -> [[1], [0.5, 0.5]]
    # 3 -> [[1], [1  , 1  ]]
    # 4 -> [[1], [1  , 1  ], [0.25, 0.5, 0.25]]
