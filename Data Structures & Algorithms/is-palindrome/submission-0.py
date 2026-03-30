class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_string = "".join(filter(str.isalnum, s)).lower()
        i = 0
        j = len(alphanum_string) - 1

        while i < j:
            if alphanum_string[i] != alphanum_string[j]:
                return False
            i += 1
            j -= 1

        return True
