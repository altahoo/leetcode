# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        result = []
        p_counter = [0] * 256
        s_counter = [0] * 256
        for i in range(len(p)):
            p_counter[ord(p[i])] += 1
            s_counter[ord(s[i])] += 1
        
        if p_counter == s_counter:
            result.append(0)
        
        for i in range(len(p), len(s)):
            s_counter[ord(s[i])] += 1
            s_counter[ord(s[i - len(p)])] -= 1
            if s_counter == p_counter:
                result.append(i - len(p) + 1)

        return result