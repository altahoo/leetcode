# 10. Regular Expression Matching

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1:
            return len(s) == 1 and (s == p or p == '.')
        if p[1] != '*':
            if not s:
                return False
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        
        while s and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])