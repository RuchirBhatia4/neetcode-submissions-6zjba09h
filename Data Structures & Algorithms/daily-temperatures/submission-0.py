class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        i = 0
        while i < len(temperatures):
            j = i
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    l.append(j-i)
                    break
                j += 1
                if j == len(temperatures):
                    l.append(0)
            i += 1
        return l