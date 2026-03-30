class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer_list = []
        for i in range(0, len(nums)):
            product = 1
            for j in range(0, len(nums)):
                if j == i:
                    continue
                else:
                    product = product * nums[j]
            answer_list.append(product)
        return answer_list
        