# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.strip().split(' ')[::-1]:
            if word.strip():
                result.append(word.strip())
        return ' '.join(result)
