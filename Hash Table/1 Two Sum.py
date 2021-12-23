# Hash Table
def two_sum(nums, target):
    # 這裡使用dictionary，
    # 因為for the purpose of an interview, we often just summarize that
    # getting and setting in a hash table is constant time.(O(1))
    # 所以此解法最終時間複雜度為O(n)
    lookup = {}
    for i in range(len(nums)):
        if target-nums[i] not in lookup:
            lookup[nums[i]] = i
        else:
            return [lookup[target-nums[i]], i]


if __name__ == '__main__':
    nums_input = [1, 2, 3]
    target_input = 4
    print(two_sum(nums_input, target_input))
