# 224. Basic Calculator

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        "(1+(4+5+2)-3)+(6+8)"
        cur, output, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in '+-':
                output += cur * sign
                cur = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c == '(':
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ')':
                output += (cur * sign)
                output *= stack.pop()
                output += stack.pop()
                cur = 0
        return output + cur * sign