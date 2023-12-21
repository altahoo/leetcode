# 241. Different Ways to Add Parentheses

# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10


class Solution:

    memo = {}
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        result = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for _, l_num in enumerate(left):
                    for _, r_num in enumerate(right):
                        if char == '+':
                            result.append(l_num + r_num)
                        elif char == '-':
                            result.append(l_num - r_num)
                        else:
                            result.append(l_num * r_num)
        if not result:
            result.append(int(expression))
        self.memo[expression] = result
        return result
