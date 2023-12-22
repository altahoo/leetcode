# 244. Shortest Word Distance II

# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

# Implement the WordDistance class:

# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.mapping = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.mapping[word].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        idxes1, idxes2 = self.mapping[word1], self.mapping[word2]

        i1, i2 = 0, 0
        result = float('inf')
        while i1 < len(idxes1) and i2 < len(idxes2):
            result = min(result, abs(idxes2[i2] - idxes1[i1]))
            if idxes1[i1] > idxes2[i2]:
                i2 += 1
            else:
                i1 += 1
        return result