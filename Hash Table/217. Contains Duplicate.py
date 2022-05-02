# Array, Hash Table, Sorting
# Time:O(n), We do search() and insert() for n times and each operation takes constant time.
# Space:O(n), The space used by a hash table is linear with the number of elements in it.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num not in lookup:
                lookup.add(num)
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums=nums))
