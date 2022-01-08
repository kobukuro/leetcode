# Array, Math, Two Pointers
class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k = k % len(nums)
        end = len(nums) - 1
        self.reverse(nums, 0, end - k)
        # [4, 3, 2, 1, 5, 6, 7]
        self.reverse(nums, end - k + 1, end)
        # [4, 3, 2, 1, 7, 6, 5]
        self.reverse(nums, 0, end)
        # [5, 6, 7, 1, 2, 3, 4]

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums=nums, k=3)
    print(nums)
