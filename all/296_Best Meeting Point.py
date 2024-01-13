# 296. Best Meeting Point

# Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = [], []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        
        row = rows[len(rows) // 2]
        cols.sort()
        col = cols[len(cols) // 2]

        def min_distance(points, center):
            distance = 0
            for point in points:
                distance += abs(point - center)
            return distance

        return min_distance(rows, row) + min_distance(cols, col)