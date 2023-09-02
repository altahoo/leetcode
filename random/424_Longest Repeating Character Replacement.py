# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = [0] * 26
        start = 0
        max_count = 0
        for i, cur in enumerate(s):
            count[ord(cur) - ord('A')] += 1
            max_count = max(max_count, count[ord(cur) - ord('A')])
            while (i - start + 1 - max_count > k):
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
            result = max(result, i - start + 1)
        return result