# 171. Excel Sheet Column Number

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, letter in enumerate(columnTitle[::-1]):
            result += (26 ** i) * (ord(letter) - ord('A') + 1)
        return result