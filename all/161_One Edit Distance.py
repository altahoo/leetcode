# 161. One Edit Distance

# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        def diff_one(long, short):
            for i in range(len(long)):
                if short == long[:i] + long[i + 1:]:
                    return True
            return False
        
        ls, lt = len(s), len(t)
        if ls - lt == 1:
            return diff_one(s, t)
        elif lt - ls == 1:
            return diff_one(t, s)
        elif lt == ls and s != t:
            for i in range(lt):
                if s[:i] + s[i + 1:] == t[:i] + t[i + 1:]:
                    return True
        return False