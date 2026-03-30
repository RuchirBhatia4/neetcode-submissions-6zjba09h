class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sets = set(nums)
        new_nums = list(sets)
        length_of_new_nums = len(new_nums)
        for i in range(0, length_of_new_nums):
            if nums.count(new_nums[i]) > len(nums)/2:
                return new_nums[i]