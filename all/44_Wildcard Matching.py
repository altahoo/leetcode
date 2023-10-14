# 44. Wildcard Matching

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_star = -1
        s_star = -1
        s_i, p_i = 0, 0
        while s_i < len(s):
            if p_i < len(p) and (s[s_i] == p[p_i] or p[p_i] == '?'):
                s_i += 1
                p_i += 1
            elif p_i < len(p) and p[p_i] == '*':
                p_star = p_i
                p_i += 1
                s_star = s_i
            elif s_star >= 0:
                p_i = p_star + 1
                s_star += 1
                s_i = s_star
            else:
                return False
        
        while p_i < len(p) and p[p_i] == '*':
            p_i += 1
        return p_i == len(p)