# 522. Longest Uncommon Subsequence II

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        result = -1
        n = len(strs)
        for i in range(n):
            found = False
            for j in range(n):
                if i == j:
                    continue
                if self.check_subs(strs[i], strs[j]):
                    found = True
                    break
            if not found:
                result = max(result, len(strs[i]))
        return result
    
    def check_subs(self, substr, str):
        i = 0
        for c in str:
            if c == substr[i]:
                i += 1
            if i == len(substr):
                break
        return i == len(substr)

