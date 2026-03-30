class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        max_cnt = 0
        check = ""
        i = 0
        while i < len(s):
            if s[i] not in check:
                check = check + s[i]
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                check = check[check.find(s[i]) + 1:]
                check = check + s[i]
                cnt = len(check)
            i = i + 1
        return max_cnt
            
            
                
