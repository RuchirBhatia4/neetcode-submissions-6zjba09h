class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_list = ""
        for c in order:
            if c in s:
                char_list += c * s.count(c)
        for c in char_list:
            if c in s:
                s = s.replace(c, "", 1)
                chat_list = char_list.replace(c, "", 1)
        for c in char_list:
            s += c
        return s