# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def _solve(rows, excludes):
            row = len(rows)
            if row == n:
                result.append(rows)
                return

            for col in range(n):
                if (row, col) in excludes:
                    continue
                
                ex = set()
                new_row = '.' * col + 'Q' + '.' * (n - col - 1)

                for r in range(row, n):
                    ex.add((r, col))
                
                r, l = row + 1, col + 1
                while r < n and l < n:
                    ex.add((r, l))
                    r += 1
                    l += 1
                r, l = row + 1, col - 1
                while r < n and l >= 0:
                    ex.add((r, l))
                    r += 1
                    l -= 1
                _solve(rows + [new_row], excludes | ex)

        _solve([], set())
        return result