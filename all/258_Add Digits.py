# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            result = 0
            while num:
                result += num % 10
                num //= 10
            num = result
            if num < 10:
                return num