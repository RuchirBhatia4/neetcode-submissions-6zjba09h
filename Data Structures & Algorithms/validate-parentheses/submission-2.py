class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        st = []
        match = {')': '(', ']': '[', '}': '{'}

        while i < len(s):
            ch = s[i]
            if ch in '([{':
                st.append(ch)
            else:
                if not st or st[-1] != match[ch]:
                    return False
                st.pop()
            i += 1

        return st == []
