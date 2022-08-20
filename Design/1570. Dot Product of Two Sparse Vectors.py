# Design, Array, Hash Table, Two Pointers
class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(self.arr)):
            res += self.arr[i] * vec.arr[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
