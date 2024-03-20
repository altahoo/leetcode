# 408. Valid Word Abbreviation

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a_idx = 0
        w_idx = 0
        num_start = -1
        while a_idx < len(abbr):
            print("num_start:", num_start)
            if abbr[a_idx].isnumeric():
                if num_start == -1:
                    num_start = a_idx
                if a_idx == len(abbr) - 1 or abbr[a_idx + 1].isalpha():
                    if abbr[num_start] == '0':
                        return False
                    num = int(abbr[num_start: a_idx + 1])
                    num_start = -1
                    w_idx += num
                    
                    if (a_idx == len(abbr) - 1 and w_idx > len(word)) or (a_idx != len(abbr) - 1  and w_idx >= len(word)):
                        return False

            elif abbr[a_idx].isalpha():
                if w_idx >= len(word):
                    return False
                if abbr[a_idx] != word[w_idx]:
                    return False
                w_idx += 1 
            a_idx += 1

        return w_idx == len(word)