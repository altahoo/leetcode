# 87. Scramble String

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            if sorted(s1) != sorted(s2):
                return False
            
            if len(s1) == 1:
                return True
        
            for i in range(1, len(s1)):
                if (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i])) or (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False
        
        return helper(s1, s2)