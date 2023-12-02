# 186. Reverse Words in a String II

# Given a character array s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

# Your code must solve the problem in-place, i.e. without allocating extra space.

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def _swap(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        start, end = 0, -1
        for i, item in enumerate(s):
            if item != ' ':
                continue
            end = i - 1
            _swap(start, end)
            start = i + 1
        
        if end != len(s) - 2:
            end = len(s) - 1
            _swap(start, end)
        
        start, end = 0, len(s) - 1
        _swap(start, end)
        return s