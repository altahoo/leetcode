# 32. Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        start = 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            if not stack:
                start = i + 1
                continue
            stack.pop()
            result = max(result, i - start + 1) if not stack else max(result, i - stack[0])
        return result