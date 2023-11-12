# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        
        for i in range(1, numRows):
            cur = [1]
            prev = result[-1]
            for j in range(len(prev) -  1):
                cur.append(prev[j] + prev[j + 1])
            cur.append(1)
            result.append(cur)
        return result
