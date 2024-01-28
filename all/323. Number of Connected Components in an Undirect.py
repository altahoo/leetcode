# 323. Number of Connected Components in an Undirected Graph

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        visited = [False] * n
        result = 0

        def bfs(node):
            queue = collections.deque([node])
            while queue:
                cur = queue.popleft()
                if visited[cur]:
                    continue
                visited[cur] = True
                for neighbor in graph[cur]:
                    queue.append(neighbor)

        for i in range(n):
            if not visited[i]:
                bfs(i)
                result += 1
        
        return result