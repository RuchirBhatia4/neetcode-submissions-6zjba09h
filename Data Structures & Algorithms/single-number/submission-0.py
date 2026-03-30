class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_list = 0
        for num in nums:
            sum_list += num
        
        sets = set(nums)
        sum_set = 0
        for num in sets:
            sum_set += num
        sum_set *= 2
        return sum_set - sum_list
