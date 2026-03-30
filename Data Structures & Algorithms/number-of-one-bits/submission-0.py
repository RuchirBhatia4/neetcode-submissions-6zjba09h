class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            total += 1 if n & 1 else 0
            n >>= 1
        return total