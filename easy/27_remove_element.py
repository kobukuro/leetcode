def remove_element(nums, val):
    total = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = '_'
            total -= 1
    # print(nums)
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == '_' and nums[j] != '_':
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[i] == '_' and nums[j] == '_':
            j -= 1
        elif nums[i] != '_' and nums[j] == '_':
            i += 1
            j -= 1
        else:
            i += 1
    # print(nums)
    return total


def remove_element_better_version(nums, val):
    a = 0
    b = 0

    while a < len(nums):
        if nums[a] != val:
            nums[b] = nums[a]
            b += 1
        a += 1

    return b


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    remove_element_better_version(nums=nums, val=val)
