# 318. Maximum Product of Word Lengths

# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        result = 0

        def no_common_letters(s1, s2):
            bit_number = lambda ch: ord(ch) - ord('a')
            bitmask1, bitmask2 = 0, 0
            for ch in s1:
                bitmask1 |= 1 << bit_number(ch)
            for ch in s2:
                bitmask2 |= 1 << bit_number(ch)
            return bitmask1 & bitmask2 == 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if no_common_letters(words[i], words[j]):
                    result = max(result, len(words[i]) * len(words[j]))
        return result


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bit_number = lambda ch: ord(ch) - ord('a')

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])

        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    result = max(result, lens[i] * lens[j])
        return result