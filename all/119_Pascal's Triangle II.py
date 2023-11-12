# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        if rowIndex == 0:
            return cur
        
        for i in range(rowIndex):
            prev = cur
            cur = [1]
            for j in range(len(prev) -  1):
                cur.append(prev[j] + prev[j + 1])
            cur.append(1)
        return cur
        