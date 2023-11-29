# 168. Excel Sheet Column Title

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            result += chr(65 + columnNumber % 26)
            columnNumber //= 26 
        return result[::-1]