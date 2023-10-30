# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
    
        prev1, prev2 = 1, 0
        for i in range(len(s)):
            c1 = 0
            if s[i] != '0':
                c1 = prev1
            c2 = 0
            if i >= 1 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                c2 = prev2
            prev2 = c1
            prev1 = c1 + c2
        return prev1
