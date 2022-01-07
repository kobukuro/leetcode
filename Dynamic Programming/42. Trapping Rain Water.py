# Dynamic Programming
# not efficient solution
# class Solution:
#     def trap(self, height):
#         total = 0
#         for i in range(len(height)):
#             max_left = 0
#             max_right = 0
#             if i != 0:
#                 max_left = max(height[0:i])
#             if i != len(height)-1:
#                 max_right = max(height[i+1:len(height)])
#             water_height = min(max_left, max_right)
#             if water_height >= height[i]:
#                 total += water_height - height[i]
#         return total

# two pointers solution : O(n) time, O(1) space
# reference:https://www.youtube.com/watch?v=ZI2z5pq0TqA
class Solution:
    def trap(self, height):
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        total = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                if min(max_left, max_right) - height[l] > 0:
                    total += min(max_left, max_right) - height[l]
                max_left = max(max_left, height[l])
            elif max_left > max_right:
                r -= 1
                if min(max_left, max_right) - height[r] > 0:
                    total += min(max_left, max_right) - height[r]
                max_right = max(max_right, height[r])
        return total


if __name__ == '__main__':
    # height = [4, 2, 0, 3, 2, 5]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    print(Solution().trap(height=height))
