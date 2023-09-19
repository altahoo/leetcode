# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counter = collections.defaultdict(int)
        s2_counter = collections.defaultdict(int)
        for i in range(n1):
            s1_counter[s1[i]] += 1
            s2_counter[s2[i]] += 1
        
        if s1_counter == s2_counter:
            return True

        for i in range(n1, n2):
            letter = s2[i]
            s2_counter[letter] += 1
            s2_counter[s2[i - n1]] -= 1
            if s2_counter[s2[i - n1]] == 0:
                del s2_counter[s2[i - n1]]
            
            if s2_counter == s1_counter:
                return True
        
        return False