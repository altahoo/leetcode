# 8. String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        negative = False
        if s[0] in ('+', '-'):
            negative = s[0] == '-'
            s = s[1:]
        if not s:
            return 0
        
        i = 0
        if s[0] == '0':
            while i < len(s) and s[i] == '0':
                i += 1
        if i == len(s):
            return 0
            
        s = s[i:]
        for i in range(len(s)):
            if not s[i].isdigit():
                break
        if not s[i].isdigit():
            i -= 1
        if i < 0:
            return 0
        s = int(s[: i + 1])
        if negative:
            s = -s
        if s > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if s < - 2 ** 31:
            return - 2 ** 31
        return s
        