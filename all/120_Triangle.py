# 120. Triangle

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if not n:
            return 0
        if n == 1:
            return triangle[0][0]
        
        prev_total = triangle[0]
        for i in range(1, n):
            prev = triangle[i - 1]
            cur = triangle[i]
            cur_total = []
            for j in range(len(cur)):
                if j == 0:
                    cur_total.append(cur[j] + prev_total[0])
                elif j == len(cur) - 1:
                    cur_total.append(cur[j] + prev_total[len(prev_total) - 1])
                else:
                    cur_total.append(cur[j] + min(prev_total[j - 1], prev_total[j]))
            prev_total = cur_total
        return min(prev_total)