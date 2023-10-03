# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        result = ''
        while True:
            letter = ''
            for string in strs:
                if i > len(string) - 1:
                    return result
                if not letter:
                    letter = string[i]
                    continue
                if string[i] != letter:
                    return result
            result += letter
            i += 1
        return result