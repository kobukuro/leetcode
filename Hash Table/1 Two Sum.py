# Hash Table, Array
def two_sum(nums, target):
    # 這裡使用dictionary，
    # 因為for the purpose of an interview, we often just summarize that
    # getting and setting in a hash table is constant time.(O(1))

    # Time complexity: O(n).
    # We traverse the list containing n elements only once.
    # Each lookup in the table costs only O(1) time.
    # Space complexity: O(n).
    # The extra space required depends on the number of items stored in the hash table,
    # which stores at most n elements.
    lookup = {}
    for i in range(len(nums)):
        if target - nums[i] not in lookup:
            lookup[nums[i]] = i
        else:
            return [lookup[target - nums[i]], i]


if __name__ == '__main__':
    nums_input = [1, 2, 3]
    target_input = 4
    print(two_sum(nums_input, target_input))
