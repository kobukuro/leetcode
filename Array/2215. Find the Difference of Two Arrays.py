# Array, Hash Table
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res1 = set()
        res2 = set()
        same = set()
        while i != len(nums1) and j != len(nums2):
            if nums1[i] < nums2[j]:
                if nums1[i] not in same:
                    res1.add(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                if nums2[j] not in same:
                    res2.add(nums2[j])
                j += 1
            else:
                same.add(nums1[i])
                i += 1
                j += 1
        if i != len(nums1):
            while i != len(nums1):
                if nums1[i] not in same:
                    res1.add(nums1[i])
                i += 1
        if j != len(nums2):
            while j != len(nums2):
                if nums2[j] not in same:
                    res2.add(nums2[j])
                j += 1
        return [list(res1), list(res2)]
