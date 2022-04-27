# Array, Prefix Sum
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = 1
        for i in range(len(nums)):
            result *= nums[i]
            prefix.append(result)
        print(prefix)
        result = 1
        for i in range(len(nums) - 1, -1, -1):
            result *= nums[i]
            postfix.append(result)
        postfix.reverse()
        print(postfix)
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]
        return nums
