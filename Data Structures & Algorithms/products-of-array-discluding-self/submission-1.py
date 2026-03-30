class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer_list = []
        # for i in range(0, len(nums)):
        #     product = 1
        #     for j in range(0, len(nums)):
        #         if j == i:
        #             continue
        #         else:
        #             product = product * nums[j]
        #     answer_list.append(product)
        # return answer_list
        
        # I just watched the neetcode explanation
        # Here is my attempt to solve the question using prefix and suffix
        
        output_list = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output_list[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output_list[i] *= postfix
            postfix *= nums[i]
        
        return output_list
            
            












