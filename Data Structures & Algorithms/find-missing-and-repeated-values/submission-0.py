class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = [j for sub in grid for j in sub]
        total = 0
        for i in range(1, (len(grid) * len(grid)) + 1):
            total += i
        b = list(set(a))
        return [sum(a) - sum(b), total - sum(b)]
        