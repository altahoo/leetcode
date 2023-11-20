# 140. Word Break II

# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        sol_exist = [False for _ in range(n + 1)]
        sol_exist[0] = True
        for start in range(n):
            for end in range(start + 1, n + 1):
                if sol_exist[start] and s[start:end] in wordDict:
                   sol_exist[end] = True
        
        if not sol_exist[-1]:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']

        for start in range(n):
            for end in range(start + 1, n + 1):
                if s[start:end] in wordDict:
                    for sub in dp[start]:
                        dp[end].append(sub + ' ' + s[start:end])
        return [s[1:] for s in dp[-1]]