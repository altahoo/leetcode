# 126. Word Ladder II

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList or len(beginWord) != len(endWord):
            return []

        if beginWord not in wordList:
            wordList.add(beginWord)

        unseen = wordList
        n = len(beginWord)
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(n):
                neighbors[word[:i] + '*' + word[i+1:]].append(word)
        
        # first bfs to build reversed neighbors list
        reverse_neighbors = defaultdict(list)
        q = [beginWord]
        unseen.remove(beginWord)
        while q:
            new_seen = set()
            for word in q:
                for i in range(n):
                    for neighbor in neighbors[word[:i] + '*' + word[i+1:]]:
                        if neighbor in unseen:
                            reverse_neighbors[neighbor].append(word)
                            new_seen.add(neighbor)
            q = list(new_seen)
            unseen -= new_seen
            if reverse_neighbors[endWord]:
                break
        # if endWord does not have reversed neigbors it is not reachable so return empty list
        if not reverse_neighbors[endWord]:
            return []
        
        # second bfs
        paths = [[endWord]]
        while paths[-1][0] != beginWord:
            new_paths = []
            for path in paths:
                last_node = path[0]
                for neighbor in reverse_neighbors[last_node]:
                    new_paths.append([neighbor] + path)
            paths = new_paths
        return paths