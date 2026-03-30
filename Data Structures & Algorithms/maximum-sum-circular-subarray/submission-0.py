class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + nums
        max_sum = nums[0]

        for i in range(n):
            summ = 0
            for j in range(i, i + n):
                summ += nums[j]
                if summ > max_sum:
                    max_sum = summ

        return max_sum