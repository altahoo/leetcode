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