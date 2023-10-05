# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                if char in ['(', '[', '{']:
                    stack.append(char)
                    continue
                else:
                    return False
            if stack[-1] in ['(', '[', '{']:
                if char in ['(', '[', '{']:
                    stack.append(char)
                elif (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']'):
                    stack.pop()
                else:
                    return False
        return not stack