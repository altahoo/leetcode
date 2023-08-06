# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        x, y = 0, 0
        result = []
        for i in range(m * n):
            result.append(mat[x][y])
            if x == 0 and y == n - 1 and (x + y) % 2 == 0:
                x += 1
            elif x == m - 1 and y == 0 and (x + y) % 2 == 1:
                y += 1
            elif (x + y) % 2 == 0:
                if x == 0:
                    y += 1
                elif y == n - 1:
                    x += 1
                else:
                    x -= 1
                    y += 1
            else:
                if x == m - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
        return result


sol = Solution()
sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            