# 127. Word Ladder

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord) or beginWord == endWord or endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        queue = collections.deque()
        queue.append(beginWord)
        if beginWord in wordList:
            wordList.remove(beginWord)

        characters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        n = 0
        visited = set()
        while queue:
            n += 1
            for _ in range(len(queue)):
                cur_word = queue.popleft()
                for i in range(len(cur_word)):
                    for char in characters:
                        new_word = cur_word[:i] + char + cur_word[i + 1:]
                        if new_word == endWord:
                            return n + 1
                        if new_word in visited:
                            continue
                        visited.add(new_word)
                        if new_word in wordList:
                            queue.append(new_word)
                            wordList.remove(new_word)
        return 0