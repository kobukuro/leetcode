# Array, Two Pointers, Greedy
# reference:https://www.youtube.com/watch?v=UuiTKBwPgAo
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, height):
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height=height))
