class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                depth = len(stack)
                if max_depth < depth:
                    max_depth = depth
            if c == ')' and stack != []:
                stack.pop()
        return max_depth