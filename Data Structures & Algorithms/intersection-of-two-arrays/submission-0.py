class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        if len(set_nums1) < len(set_nums2):
            for c in nums1:
                if c in nums2:
                    l.append(c)
                    print(c)
        else:
            for c in nums2:
                if c in nums1:
                    l.append(c)
        s = set(l)
        l2 = list(s)
        return l2