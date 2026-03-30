class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums2 = set(nums)
        for i in nums2:
            if nums.count(i) > 1:
                return i
        