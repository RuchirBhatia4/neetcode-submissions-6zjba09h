class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            ans.append(i.bit_count())
        return ans
        