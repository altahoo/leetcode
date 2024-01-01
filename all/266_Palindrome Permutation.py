# 266. Palindrome Permutation

# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_count = collections.Counter(s)
        odd = False
        for _, count in s_count.items():
            if count % 2 == 0:
                continue
            if odd:
                return False
            odd = True
        return True