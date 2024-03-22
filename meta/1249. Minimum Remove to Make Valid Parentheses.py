# 1249. Minimum Remove to Make Valid Parentheses

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
                result.append(i)
            elif i == ')':
                if left > 0:
                    left -= 1
                    result.append(i)
            else:
                result.append(i)
        
        
        if left == 0:
            return ''.join(result)
        
        new_result = []
        i = len(result) - 1
        while i >= 0:
            if result[i] == '(' and left > 0:
                left -= 1
            else:
                new_result.append(result[i])
            i -= 1
        
        return ''.join(new_result[::-1])