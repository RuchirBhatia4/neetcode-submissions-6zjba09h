class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l = []
        flag = True
        for i in range(0, len(heights)):
            flag = True
            for j in range(i+1, len(heights)):
                if heights[i] <= heights[j]:
                    flag = False
            if flag == True:
                l.append(i)
        return l