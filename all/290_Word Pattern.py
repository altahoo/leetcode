# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        p_to_s_mapping = {}
        s_to_p_mapping = {}
        for i, letter in enumerate(pattern):
            if letter not in p_to_s_mapping:
                p_to_s_mapping[letter] = s[i]
            if s[i] not in s_to_p_mapping:
                s_to_p_mapping[s[i]] = letter
                
            if p_to_s_mapping[letter] != s[i] or s_to_p_mapping[s[i]] != letter:
                return False

        return True