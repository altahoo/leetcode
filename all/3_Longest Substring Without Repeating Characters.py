# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = set()
        max_length = 0
        for i, char in enumerate(s):
            if char not in visited:
                max_length = max(max_length, i - left + 1)
                visited.add(char)
                continue
            while s[left] != char:
                left += 1
            left += 1
            visited = set(s[left: i + 1])
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_to_idx = {}
        max_length = 0
        for i, char in enumerate(s):
            if char not in char_to_idx or char_to_idx[char] < left:
                max_length = max(max_length, i - left + 1)
                char_to_idx[char] = i
                continue
            left = char_to_idx[char] + 1
            char_to_idx[char] = i
        return max_length