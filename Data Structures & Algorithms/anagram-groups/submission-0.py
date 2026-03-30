class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        this_dict = {}
        i = 0
        while i < len(strs):
            key = ''.join(sorted(strs[i]))
            if key in this_dict:
                this_dict[key].append(strs[i])
            else:
                this_dict[key] = [strs[i]]
            i += 1
        return list(this_dict.values())
