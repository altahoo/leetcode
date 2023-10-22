# 72. Edit Distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        # table[i][j]: minimum number of steps to convert word1[1:i] to word2[1:j], assuming string starts from 1
        table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            table[i][0] = i
        for i in range(1, len2 + 1):
            table[0][i] = i
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                delete_or_insert = min(table[i - 1][j], table[i][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = min(delete_or_insert, table[i - 1][j - 1])
                else:
                    table[i][j] = min(delete_or_insert, table[i - 1][j - 1] + 1)
        return table[len1][len2]

