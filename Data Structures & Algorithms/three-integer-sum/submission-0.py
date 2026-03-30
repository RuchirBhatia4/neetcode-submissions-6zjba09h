class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i, num in enumerate(nums):
            target = -num
            hsh = {}
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in hsh:
                    triplet = tuple(sorted([nums[i], complement, nums[j]]))
                    ans.add(triplet)
                else:
                    hsh[nums[j]] = j
        return [list(t) for t in ans]