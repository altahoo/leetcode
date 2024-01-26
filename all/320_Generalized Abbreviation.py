# 320. Generalized Abbreviation

# A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent 
# substrings and replacing them with their respective lengths.

# For example, "abcde" can be abbreviated into:
# "a3e" ("bcd" turned into "3")
# "1bcd1" ("a" and "e" both turned into "1")
# "5" ("abcde" turned into "5")
# "abcde" (no substrings replaced)
# However, these abbreviations are invalid:
# "23" ("ab" turned into "2" and "cde" turned into "3") is invalid as the substrings chosen are adjacent.
# "22de" ("ab" turned into "2" and "bc" turned into "2") is invalid as the substring chosen overlap.
# Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        n = len(word)

        def helper(cur_sol, idx):
            if idx >= n:
                result.append(cur_sol)
                return
            
            helper(cur_sol + word[idx], idx + 1)
            if cur_sol and cur_sol[-1].isnumeric():
                return
            for j in range(idx, n):
                helper(cur_sol + str(j - idx + 1), j + 1)

        helper("", 0)
        return result