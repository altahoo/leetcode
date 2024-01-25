# 317. Shortest Distance from All Buildings

# You are given an m x n grid grid of values 0, 1, or 2, where:

# each 0 marks an empty land that you can pass by freely,
# each 1 marks a building that you cannot pass through, and
# each 2 marks an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

# Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_distance = float('inf')

        total_houses = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_houses += 1

        def bfs(i, j):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = collections.deque([(i, j)])
            steps = 0
            sum_distance = 0
            visited = set()
            reached_houses = 0

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    if grid[row][col] == 1:
                        sum_distance += steps
                        reached_houses += 1
                        continue
                    
                    for x, y in dirs:
                        next_row, next_col = row + x, col + y
                        if 0 <= next_row < m and 0 <= next_col < n:
                            if (next_row, next_col) not in visited and grid[next_row][next_col] != 2:
                                visited.add((next_row, next_col))
                                queue.append((next_row, next_col))
                steps += 1
            
            if reached_houses != total_houses:
                return float('inf')
            
            return sum_distance

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    min_distance = min(min_distance, bfs(i, j))
        
        return min_distance if min_distance < float('inf') else -1