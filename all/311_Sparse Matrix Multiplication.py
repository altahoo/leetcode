# 311. Sparse Matrix Multiplication

# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i, row in enumerate(mat1):
            for j, item1 in enumerate(row):
                if item1 == 0:
                    continue
                for k, item2 in enumerate(mat2[j]):
                    result[i][k] += item1 * item2
        return result