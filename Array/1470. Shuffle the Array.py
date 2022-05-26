# Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        i = 0
        j = n
        i_curr_control = True
        while j < len(nums):
            if i_curr_control:
                output.append(nums[i])
                i_curr_control = False
                i += 1
            else:
                output.append(nums[j])
                i_curr_control = True
                j += 1
        return output
