# Array, Hash Table
def first_missing_positive(nums):
    # 出處：https://www.youtube.com/watch?v=8g78yfzMlao
    # 要找出first missing positive number，其實這個數字一定存在於[1,...len(nums)+1]裡
    # 因為負數沒有用，所以用0來取代
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
    for i in range(len(nums)):
        # 這裡取絕對值，因為有可能nums[i]已經被改成負數
        val = abs(nums[i])
        if 1 <= val <= len(nums):
            if nums[val - 1] > 0:
                nums[val - 1] *= -1  # 做個標記(將nums[val - 1]變成負數)，代表nums[i]存在於nums中
            elif nums[val - 1] == 0:
                nums[val - 1] = -1 * (len(nums) + 1)  # 隨便給個極端值
    for i in range(1, len(nums) + 1):
        if nums[i - 1] >= 0:  # 代表i沒有在nums裡
            return i
    return len(nums) + 1


if __name__ == '__main__':
    nums = [1, 2, 0]
    print(first_missing_positive(nums=nums))
