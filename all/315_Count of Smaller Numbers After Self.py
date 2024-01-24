# 315. Count of Smaller Numbers After Self

# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = collections.Counter(s)
        start = 0
        # Find the start pos
        for i in range(len(s)):
            if s[i] < s[start]:
                start = i
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                break
        
        return s[start] + self.removeDuplicateLetters(s[start:].replace(s[start], '')) if s else ''