import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target == matrix[0][0]:
            return True
        list_2d = np.array(matrix)
        l = list_2d.flatten()
        left = 0
        right  = len(l)-1
        while left < right:
            mid = (left + right) // 2
            if target == l[mid] or target == l[right]:
                return True
            elif target < l[mid]:
                right = mid
            else:
                left = mid + 1
        return False

