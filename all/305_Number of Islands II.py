# 305. Number of Islands II

# You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

# We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

# Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.root[node] == node:
            return node
        else:
            self.root[node] = self.find(self.root[node])
            return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = self.root[root1]
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = self.root[root2]
        else:
            self.root[root2] = self.root[root1]
            self.rank[root1] += 1

    def is_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        dsu = UnionFind(m * n)
        island = 0
        ans = [0] * len(positions)

        for i, (row, col) in enumerate(positions):
            if grid[row][col]:
                ans[i] = island
                continue
        
            connected = 0
            grid[row][col] = 1
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                prev_row, prev_col = row + x, col + y
                if 0 <= prev_row < m and 0 <= prev_col < n and grid[prev_row][prev_col] == 1:
                    new_land = n * row + col
                    prev_land = n * prev_row + prev_col
                    if not dsu.is_connected(new_land, prev_land):
                        connected += 1
                        dsu.union(new_land, prev_land)
            island += 1 - connected
            ans[i] = island
        
        return ans