# 286. Walls and Gates

# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            row, col = queue.popleft()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + x, col + y
                if 0 <= next_row < m and 0 <= next_col < n and rooms[next_row][next_col] == 2147483647:
                    rooms[next_row][next_col] = rooms[row][col] + 1
                    queue.append((next_row, next_col))