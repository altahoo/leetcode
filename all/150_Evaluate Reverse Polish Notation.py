# 150. Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = int(stack.pop())
                b = int(stack.pop())
                num = 0
                if token == '+':
                    num = a + b
                elif token == '-':
                    num = b - a
                elif token == '*':
                    num = a * b
                else:
                    num = abs(b) // abs(a)
                    if a * b < 0:
                        num = -num
                stack.append(str(num))
            else:
                stack.append(token)
        return int(stack[0])