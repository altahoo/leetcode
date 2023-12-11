# 212. Word Search II

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_key = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_key] = word
        
        m, n = len(board), len(board[0])

        matched_words = set()

        def backtracking(i, j, parent_node):
            letter = board[i][j]
            node = parent_node[letter]

            if word_key in node:
                matched_words.add(node[word_key])
            
            board[i][j] = '#' # visited

            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_i, next_j = i + x, j + y
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] in node:
                    backtracking(next_i, next_j, node)

            board[i][j] =  letter # restore


        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        
        return list(matched_words)
        