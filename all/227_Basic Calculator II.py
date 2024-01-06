# 227. Basic Calculator II

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        stack = []
        op = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(cur)
                elif op == '-':
                    stack.append(-cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                elif op == '/':
                    stack.append(int(stack.pop()/cur))
                
                cur = 0
                op = c
        return sum(stack)

