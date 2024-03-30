# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrom(s):
            start, end = 0, len(s) - 1
            palindrom = False
            while start < end and s[start] == s[end]:
                if s[start] != s[end]:
                    break
                start += 1
                end -= 1
            
            if (len(s) % 2 == 1 and start == end) or (len(s) % 2 == 0 and start == end + 1):
                palindrom = True

            return start, end, palindrom

        start, end, palindrom = is_palindrom(s)

        if palindrom:
            return True
        
        a = s[:start] + s[start + 1:]
        b = s[:end] + s[end + 1:]
        
        return is_palindrom(a)[2] or is_palindrom(b)[2]


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrom(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return is_palindrom(s, start + 1, end) or is_palindrom(s, start, end - 1)
            start += 1
            end -= 1

        return True