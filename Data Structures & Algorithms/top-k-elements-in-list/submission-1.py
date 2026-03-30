from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sets = set(nums)
        new_list = list(sets)
        this_dict = {}
        for i in range(0, len(new_list)):
            this_dict[new_list[i]] = nums.count(new_list[i])

        sorted_items = sorted(this_dict.items(), key=lambda x: x[1], reverse=True)

        final_list = []
        for i in range(0, k):
            final_list.append(sorted_items[i][0])
        return final_list
