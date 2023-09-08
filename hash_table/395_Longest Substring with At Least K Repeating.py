# 395. Longest Substring with At Least K Repeating Characters

# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

# if no such substring exists, return 0.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        num_chars = len(collections.Counter(s))
        result = 0
        for unique_char_cnt in range(1, num_chars + 1):
            start, end, found, cur_chars = 0, 0, 0, 0
            freq = [0] * 26
            while end < len(s):
                if cur_chars <= unique_char_cnt:
                    to_add = ord(s[end]) - ord('a')
                    freq[to_add] += 1
                    if freq[to_add] == 1:
                        cur_chars += 1
                    if freq[to_add] == k:
                        found += 1
                    end += 1
                else:
                    to_exclude = ord(s[start]) - ord('a')
                    start += 1
                    if freq[to_exclude] == k:
                        found -= 1
                    freq[to_exclude] -= 1
                    if freq[to_exclude] == 0:
                        cur_chars -= 1
                if cur_chars == unique_char_cnt and found == unique_char_cnt:
                    result = max(result, end - start)
        return result