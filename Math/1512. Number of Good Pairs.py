# Math, Array, Hash Table, Counting
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        for i in range(len(nums)):
            hash_map[nums[i]] += 1
        ans = 0
        for ele in list(hash_map.values()):
            if ele > 1:
                ans += ele * (ele - 1) // 2
        return ans
