# 159. Longest Substring with At Most Two Distinct Characters

# Given a string s, return the length of the longest substring that contains at most two distinct characters.


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0

        start = 0
        length = 0
        chars = collections.defaultdict(int)

        for i, char in enumerate(s):
            chars[char] += 1
            while len(chars) > 2:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1
            length = max(length, i - start + 1)

        return length