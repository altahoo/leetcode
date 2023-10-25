# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        t_counter = collections.Counter(t)
        result = s + '**'
        start = 0
        cnt = 0
        for i in range(len(s)):
            t_counter[s[i]] -= 1
            if t_counter[s[i]] >= 0:
                cnt += 1
            while cnt == len(t):
                if len(result) > i - start + 1:
                    result = s[start: i + 1]
                
                t_counter[s[start]] += 1
                if t_counter[s[start]] > 0:
                    cnt -= 1
                start += 1

        return '' if result.endswith('**') else result