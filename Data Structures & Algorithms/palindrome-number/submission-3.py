class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a = reversed(s)
        print(a)
        if x // 10 == 0:
            return True
        if s == s[::-1]:
            return True
        else:
            return False
