class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s)//2:
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp
            i += 1
        
        return s