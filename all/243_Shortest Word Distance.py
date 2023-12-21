# 243. Shortest Word Distance

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result = len(wordsDict)
        i1, i2 = -1, -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                result = min(result, abs(i2-i1))
        return result