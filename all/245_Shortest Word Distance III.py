# 245. Shortest Word Distance III

# Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mapping = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            mapping[word].append(i)
        
        result = float('inf')
        if word1 == word2:
            idxes = mapping[word1]
            for i in range(len(idxes)):
                for j in range(i + 1, len(idxes)):
                    result = min(result, abs(idxes[i] - idxes[j]))
        else:
            idxes1, idxes2 = mapping[word1], mapping[word2]
            i, j = 0, 0
            while i < len(idxes1) and j < len(idxes2):
                result = min(result, abs(idxes1[i] - idxes2[j]))
                if idxes1[i] < idxes2[j]:
                    i += 1
                else:
                    j += 1
        return result