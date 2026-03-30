class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            stones[-2] = stones[-1] - stones[-2]
            stones.pop()
        return stones[0]