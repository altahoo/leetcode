# 246. Strobogrammatic Number

# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            '0': '0'
        }
        
        reverse = []
        for digit in num:
            if digit not in mapping:
                return False
            reverse.append(mapping[digit])

        return ''.join(reverse[::-1]) == num