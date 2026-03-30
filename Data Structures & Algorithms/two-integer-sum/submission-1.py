class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            needed = target - nums[i]
            try:
                j = nums.index(needed, i + 1)
            except ValueError:
                j = -1

            if j != -1 and j != i:
                return [i, j]
                