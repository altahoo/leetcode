# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def _helper(i, j, idx):
            if idx == len(word):
                return True
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[idx]:
                tmp = board[i][j]
                board[i][j] = '#'
                if any(
                    [
                        _helper(i + 1, j, idx + 1),
                        _helper(i - 1, j, idx + 1),
                        _helper(i, j + 1, idx + 1),
                        _helper(i, j - 1, idx + 1)
                    ]
                ):
                    return True
                board[i][j] = tmp
            return False


        for i in range(m):
            for j in range(n):
                if _helper(i, j, 0):
                    return True
        
        return False